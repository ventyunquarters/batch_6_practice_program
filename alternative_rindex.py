def custom_rindex(input_string, substring):

#Use for loop to search and using len to look for it
    for i in range(len(input_string) - len(substring), -2, -1):
        if i >= -1 and input_string[i + 1:i + 1 + len(substring)] == substring:
            return i + 1
    return -1

# Ask user to enter a statement
user_statement = input("Enter a statement: ")
search_substring = input("Enter the substring you want to find (from the right): ")

# Find the last index of the substring
last_index = custom_rindex(user_statement, search_substring)

# Display the result
if last_index != -1:
    print(f"The last occurrence of '{search_substring}' starts at index: {last_index}")
else:
    print(f"'{search_substring}' was not found in the string.")