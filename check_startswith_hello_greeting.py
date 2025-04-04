def custom_startswith(input_string, prefix):

#Used length to check for the prefix
    if len(prefix) > len(input_string):
        return False  # Prefix cannot be longer than the string
    return input_string[:len(prefix)] == prefix

