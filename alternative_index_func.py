def custom_index(input_string, substring):

#Use len to count substring
    for i in range(len(input_string) - len(substring) + 1):
        if input_string[i:i + len(substring)] == substring:
            return i
    return -1