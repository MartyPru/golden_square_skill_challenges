def estimate_reading_time(str):
    split_string = str.split()
    words_per_min = 200
    words_per_second = round((words_per_min / 60), 3)
    if len(str) == 0:
        return 'There is no text in the provided string.'
    return f"This text will take you approximately {len(split_string) // words_per_min} minute(s) and {round(len(split_string) % words_per_second)} second(s) to read."