def make_snippet(str):
    split_string = str.split(' ')
    new_string = ' '.join(split_string[:5])
    if len(split_string) > 5:
        return new_string + '...'
    return new_string