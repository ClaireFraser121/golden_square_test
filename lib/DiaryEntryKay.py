import math

class DiaryEntryKay:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Title and contents cannot be empty")
        self.title = title
        self._contents = contents

    def format(self):
        return f"{self.title}:{self._contents}"

    def count_words(self):
        words = self._contents.split()
        return len(words)

    def reading_time(self, wpm):
        if wpm <= 0:
            raise Exception("WPM must be greater than zero")
        contents_word_count = len(self._contents_words())
        return math.ceil(contents_word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self._contents_words()
        if self._read_so_far >= len(words):
            self._read_so_far = 0

        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self._read_so_far = chunk_end
        return " ".join(chunk_words)
    
    def _contents_words(self):
        return self._contents.split()