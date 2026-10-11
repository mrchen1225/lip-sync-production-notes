# Designing a Lip-Sync Render Workflow Without Duplicate Jobs

A user clicks Generate, the request times out, and they click again. The backend might now have two paid rendering jobs for the same intended video. The problem begins before the animation model: the application needs to know whether it is retrying a request or starting a new creative attempt.

This technical guide was drafted with AI assistance for LipSyncX on October 10, 2026. The design below is an illustrative application architecture, not a description of LipSyncX's internal implementation or a vendor API contract.

## Separate the user request from the provider job

Create an application record for each intended render. Keep its identity stable while the request is being retried. A provider job identifier belongs to that record; it should not become the only evidence that the user requested something.

An illustrative record can contain:

```json
{
  "renderId": "render_example_001",
  "requestKey": "client_attempt_example_001",
  "inputRevision": "portrait_voice_v3",
  "state": "queued",
  "providerJobId": null,
  "outputLocation": null
}
```

These are example application fields. Use your provider's documented names, states, and authentication requirements when building the adapter.

Decide what counts as the same attempt. Retrying a timed-out submission should retain its request key. Changing the portrait, narration, or model creates a new input revision and may represent a new render. Scope keys to the authenticated owner so one user's key cannot retrieve another user's job.

## Persist intent before submitting work

The important boundary is between your database and the external renderer. A process can fail after persisting a row but before making the provider request, or after the provider accepts the job but before your application saves the response.

One design is a database transaction that writes the render record and an outbox event together. A worker reads the outbox and submits the job. Keep a uniqueness rule on the owner and request key so repeated client requests resolve to the same application record.

An outbox alone does not prevent duplicate provider jobs. Delivery can happen more than once. Prefer a provider's documented idempotency facility when available; if it is absent, explicitly handle the uncertain-submit case rather than assuming a retry is free.

[AWS's transactional outbox guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) explains the database-and-message consistency problem and why the consumer still needs to handle duplicate delivery.

For the reader preparing inputs manually, [LipSyncX's talking photo workflow](https://lipsyncx.com/ai-talking-photo-generator?utm_source=github&utm_medium=article&utm_campaign=webcafe_tutorials_20261010&utm_content=render-workflow) makes the portrait-and-audio pairing concrete. For integration work, begin with the [current developer documentation](https://lipsyncx.com/developers/docs) and verify the actual contract before writing a client.

## Treat timeout as uncertainty

Use separate application states for work that is waiting, work known to be processing, and submission whose outcome is unknown. Do not mark an unknown submission as a definite provider failure merely because your HTTP client stopped waiting.

A compact conceptual progression is:

```text
queued -> submitting -> processing -> succeeded
                    -> submission_unknown
                    -> failed
```

In `submission_unknown`, reconcile through a documented provider lookup, idempotency key, or support path. If the provider offers no way to determine whether it accepted the job, make that uncertainty visible and avoid an automatic new paid submission.

For status checks, an illustrative polling schedule could be 2, 4, 8, then 15 seconds, with jitter. Follow the provider's actual rate limits and retry guidance; these numbers are design examples, not a recommendation to override documented limits.

## Keep callbacks and results durable

If the provider supports callbacks, verify them using its documented signature mechanism. Expect duplicates and events arriving in an unexpected order. Store the event identity, allow only valid state transitions, and make repeated success events harmless.

When an output is available, record the exact input revision and model used. If the provider's delivery URL expires, decide whether your application needs to copy the result to controlled storage. Do not assume a temporary URL is a permanent download.

Authorize every status and download request against the render owner. Keep provider credentials on the server and avoid putting secrets or user media URLs into public logs.

## Make quality a separate checkpoint

Provider completion tells you a file was produced. It does not tell you the voice is understandable or the face remains stable.

For a first quality sample, use a short complete passage and compare the result with its source image and audio. Listen for missing words; watch the mouth during pauses; inspect the face and the final frame. An approximately 10-second sample can expose obvious input problems before a longer attempt.

Prepare pacing before submission. [Trimming the voiceover](https://lipsyncx.com/audio-trimmer?utm_source=github&utm_medium=article&utm_campaign=webcafe_tutorials_20261010&utm_content=render-workflow-audio) gives the renderer the audio you actually intend to use. Changing its speed afterward can invalidate the timing you reviewed.

## Test the uncertain paths

Before relying on the workflow, exercise these cases in a controlled environment:

- Two submissions with the same owner and request key.
- Provider acceptance followed by a lost response.
- Worker interruption before and after provider submission.
- A repeated callback and a delayed callback.
- A completed job whose output cannot yet be downloaded.
- A user requesting another user's status or output.

Record the expected behavior for each case. The central question is whether you can tell the difference between a new intended video and an uncertain retry. Solve that distinction before increasing render volume.
