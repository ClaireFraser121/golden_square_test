from lib.gratitudes import Gratitudes

"""
Initially, starts with an empty list 
"""


def test_starts_with_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []


"""
Check to see if format is working correctly
and formats to prefix only
"""


def test_formats_to_prefix_only():
    gratitudes = Gratitudes()
    gratitudes.format()
    assert gratitudes.format() == "Be grateful for: "


"""
tests adding one item
"""


def test_adds_one_item():
    gratitudes = Gratitudes()
    gratitudes.add("coffee")
    assert gratitudes.gratitudes == ["coffee"]


"""
tests adding multiple items, preserves order and uses commas
"""


def test_add_multiple_items_preserves_order_and_uses_commas():
    gratitudes = Gratitudes()
    gratitudes.add("coffee")
    gratitudes.add("sunshine")
    gratitudes.add("friends")
    assert gratitudes.gratitudes == ["coffee", "sunshine", "friends"]
