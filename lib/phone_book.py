import re

class PhoneBook():
    def __init__(self):
        self.numbers = []
    def extract_numbers(self, diary_entry):
        numbers = re.findall(r'\b[0]{1}[0-9]{10}\b', diary_entry)
        self.numbers += numbers


    def list_numbers(self):
        return self.numbers