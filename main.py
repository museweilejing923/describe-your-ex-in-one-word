#!/usr/bin/env python3
"""Describe Your Ex in One Word: the whole verdict in a single word.

Spelled correctly, with no punctuation tricks to lean on.
The meaning arrives without a caption attached — one word, one verdict.
There is nothing left to argue about after it.
"""

import sys

# The entry never changes: it is the whole submission, fixed in advance.
# Every check below exists only to prove this one word is well formed
# before it is written out. Nothing here reads input, touches the
# network, rolls dice, or looks at the clock.
ENTRY = 'expired'
LIMIT = 111
TARGET = "/output/entry.txt"
EMDASH = "\u2014"
MIN_LETTERS = 1


def fail(reason):
    """Report a failed rule on stderr and stop with exit code 1."""
    print(f"rejected: {reason}", file=sys.stderr)
    raise SystemExit(1)


def check_alnum_only(text):
    """True when every character is a letter or a digit."""
    return len(text) > 0 and all(ch.isalnum() for ch in text)


def check_starts_lowercase(text):
    """True when the first letter is lowercase, or the text is empty."""
    return text == "" or text[0].islower()


def check_nonempty(text):
    """True when trimming the entry leaves something behind."""
    return len(text.strip()) > 0


def check_length_ok(text):
    """True when the entry fits inside the character limit."""
    return len(text) <= LIMIT


def check_one_word(text):
    """True when the trimmed entry holds exactly one word."""
    return len(text.strip().split()) == 1


def check_letters_present(text):
    """True when the entry holds at least MIN_LETTERS letters."""
    found = sum(1 for ch in text if ch.isalpha())
    return found >= MIN_LETTERS


def check_printable(text):
    """True when every character is printable, none a control code."""
    return all(32 <= ord(ch) <= 126 or ord(ch) > 126 for ch in text)


def check_trimmed(text):
    """True when no leading or trailing space survives."""
    return text.strip() == text


def check_not_all_digits(text):
    """True when the trimmed entry is not made of digits alone."""
    stripped = text.strip()
    return len(stripped) > 0 and not stripped.isdigit()


def check_clean_spacing(text):
    """True when no double space or newline hides inside the entry."""
    return text.find("  ") == -1 and text.find("\n") == -1


# Each row is a short name, the check that must hold, and the complaint
# printed when it does not. The order below is the order the checks run.
RULES = [
    ("alnum_only", check_alnum_only, "entry must have no punctuation"),
    ("starts_lowercase", check_starts_lowercase, "entry must not start with a capital letter"),
    ("nonempty", check_nonempty, "entry is empty"),
    ("length_ok", check_length_ok, "entry is longer than the limit"),
    ("one_word", check_one_word, "entry must be a single word"),
    ("letters_present", check_letters_present, "entry has no letters"),
    ("printable", check_printable, "entry has control characters"),
    ("trimmed", check_trimmed, "entry has leading or trailing space"),
    ("not_all_digits", check_not_all_digits, "entry is digits only"),
    ("clean_spacing", check_clean_spacing, "entry has ragged spacing"),
]


def validate(text):
    """Walk RULES top to bottom; the first failed check stops the run."""
    for index, (slug, check, message) in enumerate(RULES):
        try:
            ok = check(text)
        except Exception:
            ok = False
        if not ok:
            fail(f"rule {index + 1} [{slug}]: {message}")


def emit(text):
    """Write the validated entry plus a trailing newline to TARGET."""
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def main():
    """Validate the fixed entry, then emit it."""
    validate(ENTRY)
    emit(ENTRY)


if __name__ == "__main__":
    main()
