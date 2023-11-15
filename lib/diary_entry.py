class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self._reading_location = 0

    def format(self):
        return f'{self.title}: {self.contents}'

    def count_words(self):
        string = self.format()
        split_string = string.split()
        return len(split_string)

    def reading_time(self, wpm):
        word_count = self.count_words()
        return int(word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        words_can_read = wpm * minutes
        split_string = self.format().split()
        if self._reading_location >= len(split_string):
            self._reading_location = 0
        string = ' '.join(split_string[self._reading_location:(self._reading_location + words_can_read)])
        self._reading_location += words_can_read
        return string
