#!/usr/bin/env python3
"""Inspect a local PCM WAV; optionally compare its start with a reference WAV.

Prepared for LipSyncX with AI drafting, October 24, 2026.
Reads only the paths supplied on the command line. No network calls or writes.
This is a numeric file check, not a listening or generated-video quality score.
"""

import argparse
import array
import hashlib
import json
from pathlib import Path
import sys
import wave


def inspect(path):
    raw = Path(path).read_bytes()
    with wave.open(str(path), "rb") as wav:
        if wav.getcomptype() != "NONE":
            raise ValueError("Use an uncompressed PCM WAV file.")
        channels, width, rate, frames = (
            wav.getnchannels(), wav.getsampwidth(), wav.getframerate(), wav.getnframes()
        )
        pcm = wav.readframes(frames)
    if len(pcm) != frames * channels * width:
        raise ValueError("WAV data is shorter than the declared frame count.")
    return {
        "channels": channels,
        "sample_rate_hz": rate,
        "bits_per_sample": width * 8,
        "frames": frames,
        "duration_seconds": frames / rate,
        "file_sha256": hashlib.sha256(raw).hexdigest(),
        "pcm_sha256": hashlib.sha256(pcm).hexdigest(),
    }, pcm


def compare(output, output_pcm, reference, reference_pcm):
    keys = ("channels", "sample_rate_hz", "bits_per_sample")
    if any(output[k] != reference[k] for k in keys):
        raise ValueError("Comparison requires matching channels, sample rate and bit depth.")
    if output["bits_per_sample"] != 16:
        raise ValueError("Sample comparison currently supports 16-bit PCM only.")
    actual, expected = array.array("h"), array.array("h")
    actual.frombytes(output_pcm)
    expected.frombytes(reference_pcm)
    if sys.byteorder != "little":
        actual.byteswap()
        expected.byteswap()
    count = min(len(actual), len(expected))
    differences = [int(actual[i]) - int(expected[i]) for i in range(count)]
    extra_frames = output["frames"] - reference["frames"]
    return {
        "alignment_assumption": "reference sample zero corresponds to output sample zero",
        "compared_samples": count,
        "reference_fully_covered": len(actual) >= len(expected),
        "extra_frames_after_reference": extra_frames,
        "prefix_byte_identical": output_pcm[:len(reference_pcm)] == reference_pcm,
        "maximum_absolute_16_bit_sample_difference": max(map(abs, differences), default=0),
        "different_samples": sum(value != 0 for value in differences),
        "extra_tail_all_zero_samples": all(value == 0 for value in actual[len(expected):]) if extra_frames > 0 else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wav", help="Local output WAV to inspect")
    parser.add_argument("--reference", help="Optional local reference WAV; align its start first")
    args = parser.parse_args()
    try:
        result, pcm = inspect(args.wav)
        if args.reference:
            reference, reference_pcm = inspect(args.reference)
            result["reference_comparison"] = compare(result, pcm, reference, reference_pcm)
    except (OSError, EOFError, wave.Error, ValueError) as error:
        parser.exit(2, "Cannot inspect these inputs: " + str(error) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
