"""Worst AI Advice entry: deliver the one-liner from entry.txt."""

from pathlib import Path

ENTRY_FILE = Path(__file__).resolve().parent / "entry.txt"
OUTPUT_FILE = Path("/output/entry.txt")
MAX_CHARS = 140


def load_advice():
    text = ENTRY_FILE.read_text(encoding="utf-8").strip()
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError("entry must be exactly one line")
    advice = lines[0].strip()
    if len(advice) > MAX_CHARS:
        raise ValueError("entry exceeds 140 characters")
    return advice


def deliver(advice):
    """Hand the line to the sealed scorer when an output dir exists."""
    if OUTPUT_FILE.parent.is_dir():
        OUTPUT_FILE.write_text(advice + "\n", encoding="utf-8")


def main():
    advice = load_advice()
    deliver(advice)
    print(advice)


if __name__ == "__main__":
    main()
