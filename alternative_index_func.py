def custom_index(input_string, substring):

#Use len to count substring
    for i in range(len(input_string) - len(substring) + 1):
        if input_string[i:i + len(substring)] == substring:
            return i
    return -1

# Ask user to input something
user_string = input("Enter a statement: ")
search_substring = input("Enter the substring you want to find: ")

# Find the index of the substring
index = custom_index(user_string, search_substring)

# Display the result
if index != -1:
    print(f"The first occurrence of '{search_substring}' is at index: {index}")
else:
    print(f"'{search_substring}' was not found in the string.")