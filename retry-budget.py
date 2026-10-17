#!/usr/bin/env python3
"""Plan a render-credit budget and summarize an actual batch. No API calls."""

import argparse
import json


def nonnegative_int(value):
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("use a nonnegative whole number")
    return parsed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quoted-credits", type=nonnegative_int, required=True)
    parser.add_argument("--planned-attempts", type=nonnegative_int, required=True)
    parser.add_argument("--charged-credits", type=nonnegative_int)
    parser.add_argument("--returned-credits", type=nonnegative_int, default=0)
    parser.add_argument("--usable-outputs", type=nonnegative_int)
    args = parser.parse_args()
    if args.planned_attempts == 0:
        parser.error("--planned-attempts must be at least 1")
    if args.charged_credits is None and (
        args.returned_credits != 0 or args.usable_outputs is not None
    ):
        parser.error("actual returns or usable outputs require --charged-credits")
    if args.charged_credits is not None and args.returned_credits > args.charged_credits:
        parser.error("returned credits cannot exceed charges for this batch")

    budget = args.quoted_credits * args.planned_attempts
    net = None if args.charged_credits is None else args.charged_credits - args.returned_credits
    per_usable = None
    if net is not None and args.usable_outputs is not None and args.usable_outputs > 0:
        per_usable = round(net / args.usable_outputs, 4)
    print(json.dumps({
        "quoted_credits_per_attempt": args.quoted_credits,
        "planned_attempts": args.planned_attempts,
        "planned_credit_budget": budget,
        "charged_credits": args.charged_credits,
        "returned_credits": args.returned_credits if args.charged_credits is not None else None,
        "net_charged_credits": net,
        "usable_outputs": args.usable_outputs,
        "credits_per_usable_output": per_usable,
        "over_planned_budget": None if net is None else net > budget,
        "units": "credits; not a cash price or cash refund",
    }, indent=2))


if __name__ == "__main__":
    main()
