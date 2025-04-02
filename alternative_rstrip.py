#Use custom string to remove any space of character at the end of the string without using rstrip
def custom_rstrip_alt(input_string):
    if not input_string:
        return ""

#Use for loop and length to remove the space
    for i in range(len(input_string) - 1, -1, -1):
        if not input_string[i].isspace():
            return input_string[:i + 1]
    return ""
