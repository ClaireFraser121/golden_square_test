from lib.phone_book import PhoneBook

"""
Initially there are no phone numbers
"""
def test_initially_no_phone_numbers():
    phone_book = PhoneBook()
    assert phone_book.list_numbers() == []



"""
where we add a diary entry with no phone number in it
There are no phone numbers reflected in the list
"""
def test_add_entry_with_no_phone_number():
    phone_book = PhoneBook()
    phone_book.extract_numbers("No phone number here.")
    assert phone_book.list_numbers() == []

"""
When we add a diary entry with a phone number in it
The phone number is reflected in the list
"""
def test_extract_numbers_from_single_entry():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Sarah's number is 07900000003")
    assert phone_book.list_numbers() == ["07900000003"]


"""
When we add three diary entries with phone numbers in then
We see all phone numbers reflected in the list
"""
def test_extract_numbers_from_multiple_entries():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Sarah's number is 07900000003")
    phone_book.extract_numbers("Geoff's number is 07900000001")
    phone_book.extract_numbers("Alex's number is 07900000002")
    assert phone_book.list_numbers() == ["07900000003", "07900000001", "07900000002"]


"""
When we add entry with multiple numbers in it 
We see all phone numbers reflected in the list
"""
def test_extract_multiple_numbers_from_single_entry():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Sarah's number is 07900000003 and Geoff's number is 07900000001")
    assert phone_book.list_numbers() == ["07900000003", "07900000001"]

"""
When we add entry with an 11-digit number that doesn't 
    start with a zero
It is ignored in the numbers list
"""

# Missing example: should not count numbers that don't start with a zero
def test_ignores_numbers_that_dont_start_with_zero():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My friend's number is 18900000000")
    assert phone_book.list_numbers() == []

"""
When we add entry with an invalid phone number that isn't 11 digits long
It is ignored in the numbers list
"""

# Missing example: should not count numbers that aren't 11 digits long
def test_invalid_phone_number_is_not_11_digits_long():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Not good: 01 0 079000000000000000 7700")
    assert phone_book.list_numbers() == []

