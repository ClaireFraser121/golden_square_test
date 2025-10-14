from lib.gratitudes_2 import Gratitudes_2

"""
Given mulitple gratitudes
We can see a nice list of them
"""


def test_mulitple_gratitudes():
    gratitudes = Gratitudes_2()
    gratitudes.add("my cat")
    gratitudes.add("the sun")
    gratitudes.add("my friends")
    result = gratitudes.format()
    assert result == "I am grateful for: my cat, the sun, and my friends."
