from lib.report_length import report_length

"""
If the report length is correct
Return ' This string was x characters long'
"""


def test_with_correct_length():
    str = "This string was 32 characters long."
    expected = f"This string was {len(str)} characters long."
    assert report_length(str) == expected
