def count_words(str):
    if len(str) == 0:
        return 0
    words = str.split(' ')
    return len(words)