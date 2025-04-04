def custom_islower(input_string):
#Used an args for the characters
    for char in input_string:
        if 'A' <= char <= 'Z':
            return False #If any uppercase is found it will return False
        elif char.isalpha() and not ('a' <= char <= 'z'):
            return False #If its an alphabet but not lowercase
    return True
