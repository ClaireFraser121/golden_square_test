# lib/GrammarStats.py
"""
GrammarStats: tiny helper for basic sentence quality checks.

Rules this class enforces:
- A "good" sentence:
  1) begins with a capital letter (A–Z)
  2) ends with a sentence terminator: '.', '!' or '?'

We also keep stats across all checks, so you can ask:
- What percentage of checked texts were good? (as an int percentage)

Design notes for Level 4:
- Keep state in the object (self._total, self._good).
- Keep each method small and single-purpose.
- Validate inputs early (empty strings should raise).
"""

class GrammarStats:
    def __init__(self):
        # Running totals so percentage_good() can compute a percentage
        self._total = 0
        self._good = 0

    def check(self, text: str) -> bool:
        """
        Parameters:
            text (str): the text to check

        Returns:
            bool: True if `text` starts with a capital letter and ends with
                  '.', '!' or '?', otherwise False.

        Side-effects:
            - Updates internal counters for percentage_good()

        Why we strip whitespace:
            Users often include stray spaces. We don't want a trailing space
            to break the "ends with punctuation" rule.
        """
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        # Treat purely-empty or whitespace-only as invalid input.
        if text.strip() == "":
            raise ValueError("text cannot be empty")

        stripped = text.strip()

        # Rule 1: first character must be a capital A–Z
        starts_with_capital = stripped[0].isalpha() and stripped[0].upper() == stripped[0]

        # Rule 2: last character must be a sentence-ending punctuation mark
        ends_with_terminator = stripped[-1] in ".!?"

        is_good = starts_with_capital and ends_with_terminator

        # Update stats
        self._total += 1
        if is_good:
            self._good += 1

        return is_good

    def percentage_good(self) -> int:
        """
        Returns:
            int: percentage (0–100) of texts that passed `check`, rounded down.

        Why floor (round down)?
            Makers katas generally expect an integer percentage without
            over-promising. e.g. 2 good out of 3 => 66% (not 67%).

        Errors:
            - If nothing has been checked yet, there is no percentage to report.
        """
        if self._total == 0:
            raise RuntimeError("no texts have been checked yet")
        # Integer division after scaling by 100 floors the result naturally.
        return (self._good * 100) // self._total
