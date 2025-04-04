def custom_islower(input_string):
#Used an args for the characters
    for char in input_string:
        if 'A' <= char <= 'Z':
            return False #If any uppercase is found it will return False
        elif char.isalpha() and not ('a' <= char <= 'z'):
            return False #If its an alphabet but not lowercase
    return True

#Ask user to input a statement
user_statement = input("Enter a statement: ")

# Check if the statement is all lowercase
is_lowercase = custom_islower(user_statement)

# Display the result
print("Is the statement all lowercase?", is_lowercase)