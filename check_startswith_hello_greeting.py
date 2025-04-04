def custom_startswith(input_string, prefix):

#Used length to check for the prefix
    if len(prefix) > len(input_string):
        return False  # Prefix cannot be longer than the string
    return input_string[:len(prefix)] == prefix

# Ask user for a statement
user_statement = input("Enter a statement: ")

# Check if the statement starts with "hello" (case-insensitive)
starts_with_hello = custom_startswith(user_statement.lower(), "hello")

# Respond with True or False
print(starts_with_hello)