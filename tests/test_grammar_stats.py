# tests/test_grammar_stats.py
import pytest
from lib.GrammarStats import GrammarStats

# ---------- check() happy-path cases ----------

def test_check_good_with_period():
    gs = GrammarStats()
    assert gs.check("Hello world.") is True

def test_check_good_with_exclamation():
    gs = GrammarStats()
    assert gs.check("Wow!") is True

def test_check_good_with_question_mark_and_spaces():
    gs = GrammarStats()
    assert gs.check("   Are we there yet?   ") is True

# ---------- check() failing cases ----------

def test_check_fails_without_capital():
    gs = GrammarStats()
    assert gs.check("no capital here.") is False

def test_check_fails_without_terminator():
    gs = GrammarStats()
    assert gs.check("Missing punctuation") is False

def test_check_fails_both_rules():
    gs = GrammarStats()
    assert gs.check("oops") is False

# ---------- check() input validation ----------

def test_check_raises_on_empty_string():
    gs = GrammarStats()
    with pytest.raises(ValueError) as err:
        gs.check("")
    assert "cannot be empty" in str(err.value)

def test_check_raises_on_whitespace_only():
    gs = GrammarStats()
    with pytest.raises(ValueError):
        gs.check("   \t  \n  ")

def test_check_raises_on_non_string():
    gs = GrammarStats()
    with pytest.raises(TypeError):
        gs.check(123)  # type: ignore

# ---------- percentage_good() ----------

def test_percentage_good_tracks_across_calls_and_floors():
    gs = GrammarStats()
    # 2 good out of 3 => 66.66...% => floor to 66
    assert gs.check("Good one.") is True
    assert gs.check("Also Good!") is True
    assert gs.check("bad ending") is False
    assert gs.percentage_good() == 66

def test_percentage_good_0_percent():
    gs = GrammarStats()
    gs.check("bad")          # False (no cap, no punctuation)
    gs.check("bad.")        # False (no capital)
    gs.check("also bad!")   # False (no capital)
    assert gs.percentage_good() == 0

def test_percentage_good_100_percent():
    gs = GrammarStats()
    gs.check("All Good.")   # True
    gs.check("Yes!")        # True
    gs.check("Okay?")       # True
    assert gs.percentage_good() == 100

def test_percentage_good_raises_if_no_checks_yet():
    gs = GrammarStats()
    with pytest.raises(RuntimeError) as err:
        gs.percentage_good()
    assert "no texts have been checked" in str(err.value)

# ---------- extra edge behaviour ----------

def test_leading_quote_still_needs_capital_letter_after_it():
    gs = GrammarStats()
    # This fails because the first char is a quote, not a capital letter.
    # Keeping the rule simple for this exercise.
    assert gs.check('"Hello."') is False

def test_leading_spaces_dont_break_rules():
    gs = GrammarStats()
    assert gs.check("   Hello there!") is True
