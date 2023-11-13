def verify_text(str):
    if len(str) == 0:
        return 'Invalid - empty string.'
    
    if str[0].isupper() and str[-1] in '.!?':
        return 'Valid - string meets criteria.'
    elif not str[0].isupper():
        return 'Invalid - does not begin with capital letter.'
    elif str[-1] not in '.!?':
        return 'Invalid - does not have ending punctuation.'