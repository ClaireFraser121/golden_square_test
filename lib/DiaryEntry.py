import math

class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self._cursor = 0 # for reading_chunk method

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}\n\n{self.contents}"

    def count_words(self) -> int:
        # Returns:
        #   int: the number of words in the diary entry
        # Empty or whitespace-only contents -> 0
        if not self.contents:
            return 0
        return len(self.contents.split())

    def reading_time(self, wpm: int) -> int:
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        # validate wpm if your tests require it
        # if wpm <= 0: raise ValueError("wpm must be positive")

        # 1) Validate input (avoids divide-by-zero / nonsense)
        if not isinstance(wpm, int):
            raise TypeError("wpm must be a int")
        if wpm <=0:
            raise ValueError("wpm must be positive")
        
        # 2) Get the word count from the *single source of truth*
        total_words = self.count_words()
        return math.ceil(total_words / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        # validate wpm if your tests require it
    
            words_to_read = wpm * minutes
            all_words = self.contents.split()
            chunk = all_words[self._cursor : self._cursor + words_to_read]
            self._cursor += words_to_read
            return " ".join(chunk)
