def contains_todo(str):
    if len(str) == 0:
        return 'Please provide some text.'
    elif '#TODO' in str:
        return True
    return False