import math

class DiaryEntryKay:
    def __init__(self, title, contents):
        if title == "":
            raise Exception("Title cannot be empty")
        if contents == "":
            raise Exception("Contents cannot be empty")
        self.title = title
        self._contents = contents
        self._read_so_far = 0  # needed for reading_chunk state

    def format(self):
        return f"{self.title}: {self._contents}"

    def count_words(self):
        return len(self._contents.split())  # contents-only per usual spec

    def reading_time(self, wpm):
        if wpm <= 0:
            raise Exception("WPM must be greater than zero")
        contents_word_count = len(self._contents_words())
        return math.ceil(contents_word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        if wpm <= 0 or minutes <= 0:
            return ""  # or raise, depending on spec
        words_user_can_read = wpm * minutes
        words = self._contents_words()

        if self._read_so_far >= len(words):
            self._read_so_far = 0

        chunk_start = self._read_so_far
        chunk_end = min(chunk_start + words_user_can_read, len(words))
        chunk_words = words[chunk_start:chunk_end]
        self._read_so_far = chunk_end

        if self._read_so_far >= len(words):
            self._read_so_far = 0

        return " ".join(chunk_words)

    def _contents_words(self):
        return self._contents.split()
