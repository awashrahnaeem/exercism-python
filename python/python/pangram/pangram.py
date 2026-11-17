"""Check whether a sentence contains every English alphabet letter."""


def is_pangram(sentence):
    """Return whether the sentence contains every letter of the alphabet.

    The function ignores case and skips non-English letters while checking
    whether all 26 English letters appear at least once.
    """
    seen = set()

    for letter in sentence:
        normalized_letter = letter.lower()

        if len(normalized_letter) == 1 and 'a' <= normalized_letter <= 'z':
            seen.add(normalized_letter)

    return len(seen) == 26