def custom_count(input_string, substring):  #input_string for the searching and substring to count    count = 0
    i = 0
    while i <= len(input_string) - len(substring):
        if input_string[i:i + len(substring)] == substring:
            count += 1
            i += len(substring)  # Move past the found substring to avoid overcounting overlapping occurrences
        else:
            i += 1
    return count
