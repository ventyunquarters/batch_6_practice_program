def custom_rindex(input_string, substring):

#Use for loop to search and using len to look for it
    for i in range(len(input_string) - len(substring), -2, -1):
        if i >= -1 and input_string[i + 1:i + 1 + len(substring)] == substring:
            return i + 1
    return -1