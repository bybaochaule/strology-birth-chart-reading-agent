#!/usr/bin/env python3
"""Check whether an astrology intake JSON file has enough data for common reading types.

This helper is deterministic and does not calculate astrological placements.
It only reports missing fields and uncertainty notes.

Example:
    python scripts/example_helper.py intake.json --reading-type full
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

READING_REQUIREMENTS = {
    "placements": ["placements"],
    "big-three": ["sun", "moon", "rising"],
    "full": ["birth_date", "birth_time", "birthplace"],
    "no-time": ["birth_date", "birthplace"],
}

UNCERTAIN_WITHOUT_TIME = [
    "rising sign",
    "houses",
    "angles",
    "chart ruler",
    "some Moon details",
]


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"error: file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"error: invalid JSON: {exc}")
    if not isinstance(data, dict):
        raise SystemExit("error: intake JSON must be an object")
    return data


def value_present(data: dict[str, Any], field: str) -> bool:
    value = data.get(field)
    if value is None:
        return False
    if isinstance(value, str) and not value.strip():
        return False
    if isinstance(value, (list, dict)) and not value:
        return False
    return True


def check_intake(data: dict[str, Any], reading_type: str) -> dict[str, Any]:
    required = READING_REQUIREMENTS[reading_type]
    missing = [field for field in required if not value_present(data, field)]
    has_birth_time = value_present(data, "birth_time") or value_present(data, "rising")
    notes: list[str] = []

    if reading_type == "no-time" or not has_birth_time:
        notes.append(
            "Without exact birth time, caveat uncertainty for: "
            + ", ".join(UNCERTAIN_WITHOUT_TIME)
            + "."
        )

    if value_present(data, "full_name"):
        notes.append("Privacy note: full legal name is not needed for a chart reading.")

    return {
        "reading_type": reading_type,
        "ready": not missing,
        "missing_fields": missing,
        "notes": notes,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate astrology birth chart reading intake JSON.")
    parser.add_argument("json_file", type=Path)
    parser.add_argument(
        "--reading-type",
        choices=sorted(READING_REQUIREMENTS),
        default="full",
        help="Type of reading requested.",
    )
    args = parser.parse_args(argv)

    data = load_json(args.json_file)
    result = check_intake(data, args.reading_type)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ready"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
