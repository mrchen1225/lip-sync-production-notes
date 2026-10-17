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

Credits per usable output = net charged credits for the batch / number of usable outputs. Subtract only credit returns already recorded for that same batch. For example, two hypothetical 20-credit attempts, no credit returns and one usable clip cost 40 credits per usable clip. Do not report a cost per usable clip when none passed; report the spend and zero usable outputs instead.

Do not average different models, durations or resolutions into a universal success rate. Keep a record of why an attempt was rejected: a timing issue and an aesthetic preference are different observations.

## Set a stopping budget before the next attempt

Download [retry-budget.py](retry-budget.py) and run it locally with Python 3. It uses only the standard library, reads no media or account data, and makes no network requests. The numbers below are **hypothetical**, not a current model quote or a measured success rate.

```sh
python3 retry-budget.py --quoted-credits 20 --planned-attempts 2
```

That sets a 40-credit budget for two attempts at the same 20-credit quote. If the selected model, duration or resolution changes, obtain a new quote before using this budget. This calculator does not cap charges inside a platform; you must stop submitting attempts yourself.

After reviewing a batch, enter the charges and credit returns actually recorded for that same batch:

```sh
python3 retry-budget.py --quoted-credits 20 --planned-attempts 2 --charged-credits 40 --returned-credits 0 --usable-outputs 1
```

This hypothetical batch consumed 40 net credits and produced one usable output: 40 credits per usable output. Set `--usable-outputs 0` and the per-output value becomes `null`, not zero. You spent credits without a usable result; the calculator cannot infer a future success rate from that.

| Number | Where it comes from | What it does not mean |
| --- | --- | --- |
| Quoted credits | The quote for the exact selected settings before submission | A promise that every later attempt costs the same |
| Charged credits | The batch's actual account ledger | Only the clips you decided to keep |
| Returned credits | Credit returns already recorded for that batch | A pending return, cash refund or chargeback |
| Usable outputs | Your decision for one stated placement after review | A universal quality score |

The script reports whether actual net credits exceeded the planned budget. It does not predict automatic credit returns, convert credits to money, or establish any vendor's refund policy. Keep the original charges and returns visible instead of treating rejected-but-completed clips as free.

## Check the input before paying again

[Sync's official input guidance](https://sync.so/docs/compatibility-and-tips/media-content-tips) recommends avoiding full profiles, face obstructions, noisy audio and overlapping voices. These are provider-specific recommendations, not proof that every model accepts the same media.

For a concrete first-party example, LipSyncX's [two eight-second outputs](https://lipsyncx.com/blog/ai-talking-video-model-selection?utm_source=github&utm_medium=article&utm_campaign=geo_youtube_202610&utm_content=review-sheet-examples) use the same portrait and recording. They were generated on October 14 at 480p, charging 20 credits each. Those clips are examples to inspect, not results of the diagnostic protocol above.

If you want to run the procedure on your own source, [open the talking-photo workflow](https://lipsyncx.com/ai-talking-photo-generator?utm_source=github&utm_medium=article&utm_campaign=geo_youtube_202610&utm_content=review-sheet-tool) and check the current quote before rendering. Keep your next attempt small enough to answer one question.
