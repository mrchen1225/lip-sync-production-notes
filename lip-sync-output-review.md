# A Repeatable Review Sheet for AI Lip-Sync Outputs

When two renders look different, “better” is too vague to explain why. Keep the source, audio and duration fixed, then record the exact word or frame where an output becomes distracting. This guide provides a small review protocol and a CSV you can reuse.

Disclosure: prepared for LipSyncX with AI drafting on October 17, 2026. The protocol is a proposed manual review method, not a validated quality metric or a claim about LipSyncX's internal architecture. No new paid renders were made for this article.

## Separate file problems from generation problems

Download the result and check it locally before judging a hosted preview. If the downloaded original is synchronized and the edited export is not, inspect that editing/export path. Rerendering with another model changes too many variables to locate that issue.

Use three labels:

- **Constant offset:** voice leads or follows by roughly the same amount at the beginning and end. Test a track shift on a duplicate timeline.
- **Growing mismatch:** timing separates over the clip. Check duration and speed changes before attempting a single global shift.
- **Mouth-shape mismatch:** the timing seems plausible but a visible closure is missing, or teeth/jaw change unnaturally. A track shift cannot redraw the face.

These are diagnostic categories, not guaranteed causes. At 30 fps, one frame is approximately 33 ms; this is a measurement unit, not a pass/fail threshold.

## Make the comparison reproducible

Use a 5–10-second diagnostic segment with a readable face and one clear voice. Record the exact source file/revision, audio revision, model label, output resolution and quoted credits. Change one variable per attempt.

Magic Hour's [four-tool demonstration, from 0:38](https://www.youtube.com/watch?v=llz5KhkquyI&t=38s), uses one 15-second video and audio across its comparison. That method is useful; its rankings are a vendor's own assessment because Magic Hour sells one of the tools.

Review normal playback at the intended display size first. Use half-speed or individual frames only to locate an issue. Keep the observations separate:

| Field | What to record |
| --- | --- |
| Timing | First distracting word and timestamp; constant or changing mismatch |
| Mouth shape | A word containing an obvious closure; what looked wrong |
| Identity | Teeth, jaw, beard, outline changes |
| Performance | Expression relative to the line; unwanted camera/head motion |
| Decision | Usable for the intended placement, or reason rejected |
| Cost | Credits spent across all attempts, including rejected outputs |

## Copy the review sheet

The companion [review-sheet.csv](review-sheet.csv) contains headers and one clearly hypothetical example row. Replace the example with your actual observations. No customer data or generated-media URLs are included.

Credits per usable output = total charged credits / number of usable outputs. For example, two hypothetical 20-credit attempts yielding one usable clip cost 40 credits per usable clip. Do not report a cost per usable clip when none passed; report the spend and zero usable outputs instead.

Do not average different models, durations or resolutions into a universal success rate. Keep a record of why an attempt was rejected: a timing issue and an aesthetic preference are different observations.

## Check the input before paying again

[Sync's official input guidance](https://sync.so/docs/compatibility-and-tips/media-content-tips) recommends avoiding full profiles, face obstructions, noisy audio and overlapping voices. These are provider-specific recommendations, not proof that every model accepts the same media.

For a concrete first-party example, LipSyncX's [two eight-second outputs](https://lipsyncx.com/blog/ai-talking-video-model-selection?utm_source=github&utm_medium=article&utm_campaign=geo_youtube_202610&utm_content=review-sheet-examples) use the same portrait and recording. They were generated on October 14 at 480p, charging 20 credits each. Those clips are examples to inspect, not results of the diagnostic protocol above.

If you want to run the procedure on your own source, [open the talking-photo workflow](https://lipsyncx.com/ai-talking-photo-generator?utm_source=github&utm_medium=article&utm_campaign=geo_youtube_202610&utm_content=review-sheet-tool) and check the current quote before rendering. Keep your next attempt small enough to answer one question.
