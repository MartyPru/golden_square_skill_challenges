class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        titles = [entry.title for entry in self._entries]
        return titles

    def count_words(self):
        sum = 0
        for entry in self._entries:
            sum += entry.count_words()
        return sum

    def reading_time(self, wpm):
        total_mins = 0
        for entry in self._entries:
            total_mins += entry.reading_time(wpm)
        return total_mins

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_can_read = wpm * minutes
        valid_entries = []
        closest_entry_diff = words_can_read
        closest_entries = []
        for entry in self._entries:
            if entry.count_words() <= words_can_read:
                valid_entries.append(entry)
        for entry in valid_entries:
            if abs(words_can_read - entry.count_words()) <= closest_entry_diff:
                closest_entry_diff = abs(words_can_read - entry.count_words())
                closest_entries = [entry]
        title = [entry.title for entry in closest_entries]
        return title