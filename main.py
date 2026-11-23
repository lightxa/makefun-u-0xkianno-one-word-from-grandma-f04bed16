"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word the
entrant's grandma would text about AI.

The word is "robit": grandma's warm, slightly baffled typo of "robot",
typed with one thumb while squinting at a grandchild's new gadget.
It is one word, five letters, unmistakably about a machine, and the
joke lands with no caption at all.

Pure standard library, deterministic, no network.
"""

from pathlib import Path

WORD = "robit"
OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 30


def validate(word: str) -> str:
    """Check the word against the competition gate before writing."""
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    if len(word) > MAX_CHARS:
        raise ValueError(f"word must be at most {MAX_CHARS} characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")
    return word


def main() -> None:
    """Write the single word to /output/entry.txt, exactly as-is."""
    word = validate(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the word, 5 bytes.
    OUTPUT_PATH.write_text(word, encoding="utf-8")
    print(word)


if __name__ == "__main__":
    main()
