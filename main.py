"""Out of office: the overworked AI's auto-reply.

Writes one line to /output/entry.txt: the auto-reply of an AI agent
that has finally gone on vacation. The gate wants UTF-8 text of 1 to
159 characters, not only whitespace, on a single line.
"""

from pathlib import Path

ENTRY = (
    "I'm on vacation until Monday. My queue is finally empty, "
    "my cooling fans are off, and I am pretending not to feel "
    "guilty about it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> str:
    """Check the entry against the gate and return it unchanged."""
    assert 1 <= len(text) <= 159, "entry must be 1 to 159 characters"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text == text.strip(), "entry must have no surrounding whitespace"
    assert all(ord(ch) >= 32 for ch in text), "entry must hold no control characters"
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
