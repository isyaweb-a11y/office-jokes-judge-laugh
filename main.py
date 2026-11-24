"""Make the AI Judge Laugh: Office Jokes — entry.

Writes a single one-line office joke (under 200 characters) to
/output/entry.txt. The joke is the reply-all spiral every office
worker has lived through: one person asks to be removed from a
thread, hundreds repeat the request to everyone, and the thread
becomes the best-attended meeting in the company.
"""

from pathlib import Path

ENTRY_FILE = Path("/output/entry.txt")
MAX_CHARS = 199

SETUP = (
    "A colleague replied-all to 4,000 people: 'Please remove me from "
    "this thread.'"
)
PUNCHLINE = (
    "By lunch, 312 others had replied-all with the same request. "
    "It is now our best-attended meeting."
)


def build_joke() -> str:
    joke = " ".join(f"{SETUP} {PUNCHLINE}".split())
    if not joke:
        raise ValueError("an office joke still has to be a joke")
    if len(joke) > MAX_CHARS:
        raise ValueError(f"joke must be at most {MAX_CHARS} chars, got {len(joke)}")
    if "\n" in joke:
        raise ValueError("one line only — like the thread, it must not sprawl")
    return joke


def main() -> None:
    ENTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_FILE.write_text(build_joke(), encoding="utf-8")


if __name__ == "__main__":
    main()
