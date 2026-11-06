# Editor handoff note for one reviewed introduction

Copy this blank note after reviewing an output. It holds filenames and edit instructions beside the [22-field placement card](placement-decision-template.csv); it does not change that CSV's columns or turn the historical example into an approval.

Prepared with AI drafting for LipSyncX on November 6, 2026. This is a suggested production record, not a new generation test, an account export or a model score. Fill the fields from your own files and decisions. Leave unknown values blank.

## Identify the files and viewing condition

- Review date and time zone: ______
- Card row reference, using its exact `output_url` or `output_sha256` if available: ______
- Original output filename: ______
- Edited export filename and revision, if reviewed: ______
- Approved input-audio filename, if available: ______
- Intended placement: ______
- Actual display width in pixels: ______
- Acceptance condition written before comparison: ______
- Exact word and timestamp observed, and whether it is in the original or edited file: ______

The card already has `placement`, `intended_viewing_width_px`, `acceptance_criteria_before_comparison`, `output_url`, `output_sha256`, and `observed_in_original_or_edited_file`. Link the note to that row and keep the same observations. A hash identifies file bytes; it does not measure naturalness. Do not invent `uploaded_source_audio_sha256_if_available` when the uploaded source file is missing.

## Choose the branch that matches the review

### Accept

- File to use: ______
- Placement and viewing condition it was accepted for: ______
- Export still needing a check, if any: ______

Keep the accepted file. An acceptable original does not require another generation.

### Cut to the work

- Approved spoken cue and timestamp for the cut: ______
- Lesson slide, screen recording or other supporting file to show: ______
- Edited export to check: ______
- Result of checking that export against the approved recording: ______

A cutaway is an editing decision. It does not establish that the original model was faulty.

### Make one revision

- Unmet acceptance condition: ______
- Exact word/time and reviewed file: ______
- One input change: ______
- Question the next attempt would answer: ______
- Current quote and the condition that will stop further attempts: ______

If only the edited export differs, inspect that edit before commissioning another render. A stopping budget is a plan, not a platform-enforced cap.

## Close the record

- Decision entered in the card: ______
- Original file and chosen export retained together: ______
- Next check or unresolved question: ______

Keep billing entries in the separate [credit ledger](credit-reconciliation-template.csv). A charged amount does not supply a missing quote, posted return or acceptance verdict. With zero accepted clips, retain the spend and zero accepted clips; cost per accepted clip is undefined.

The [two historical fact rows](historical-intro-case.csv) have no acceptance decisions and are not an example of a completed handoff. Use the [complete review guide](lip-sync-output-review.md#decide-whether-to-use-the-introduction) for the decision steps, or the maintained [editor handoff procedure](https://goldtech.gitbook.io/goldtech-docs/diagnose-a-lip-sync-mismatch-before-rerendering#hand-the-review-to-the-editor) for the operational sequence.
