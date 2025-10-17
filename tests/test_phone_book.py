from lib.phone_book import PhoneBook

"""
Initially there are no phone numbers
"""
def test_initially_no_phone_numbers():
    phone_book = PhoneBook()
    assert phone_book.list_numbers() == []



# """
# where we add a diary entry with no phone number in it
# There are no phone numbers reflected in the list
# """
# phone_book = PhoneBook()
# phone_book.extract_numbers("My friend's number is 07900000000")
# phone_book.list_numbers() # => ["07900000000"]

# """
# When we add three diary entries with phone numbers in then
# We see all phone numbers reflected in the list
# """
# phone_book = PhoneBook()
# phone_book.extract_numbers("Sarah's number is 07900000003")
# phone_book.extract_numbers("Geoff's number is 07900000001")
# phone_book.extract_numbers("Alex's number is 07900000002")
# phone_book.list_numbers() # => ["07900000003", "07900000001", "07900000002"]


# """
# When we add entry with multiple numbers in it 
# We see all phone numbers reflected in the list
# """
# phone_book = PhoneBook()
# phone_book.extract_numbers("Sarah's number is 07900000003 and Geoff's number is 07900000001")
# phone_book.list_numbers() 
#     # => ["07900000000", "07900000000"]
