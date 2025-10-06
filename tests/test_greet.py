from lib.greet import greet


def test_greet_person_by_name():
    result = greet("Claire")
    assert result == "Hello, Claire!"
