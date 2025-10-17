# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

> As a user 
> So that I can keep track of my phone number
> I want to keep a record of all phone numbers i use in my diary entries

* We may want to look through multiple dairt entries
* Phone numbers are 11-digit numbers, starting with zero

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class PhoneBook():
    def extract_numbers(diary_entry):
        # Parameters:
        #   diary_entry: (str) a human-readable text, possibly with phone nos
        # Returns nothing
        pass


    def list_numbers(self):
        # Returns:
            # A list of strings, reprsenting phone numbers
            pass
``` 

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
Initially there are no phone numbers
"""
phone_book = PhoneBook()
phone_book.list_numbers() # => []


"""
where we add a diary entry with no phone number in it
There are no phone numbers reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("My friend's number is 07900000000")
phone_book.list_numbers() # => ["07900000000"]

"""
When we add three diary entries with phone numbers in then
We see all phone numbers reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("Sarah's number is 07900000003")
phone_book.extract_numbers("Geoff's number is 07900000001")
phone_book.extract_numbers("Alex's number is 07900000002")
phone_book.list_numbers() # => ["07900000003", "07900000001", "07900000002"]


"""
When we add entry with multiple numbers in it 
We see all phone numbers reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("Sarah's number is 07900000003 and Geoff's number is 07900000001")
phone_book.list_numbers() 
    # => ["07900000000", "07900000000"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
