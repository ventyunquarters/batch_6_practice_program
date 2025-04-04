def custom_rjust(input_string, length):

    if len(input_string) >= length:
        return input_string  # No padding needed

    padding_length = length - len(input_string)
    padding = " " * padding_length
    return padding + input_string

# Ask user to say a statement
user_statement = input("Input a statement: ")
desired_length = int(input("Enter the desired length for the output: "))

# Right-justify the statement
right_justified_statement = custom_rjust(user_statement, desired_length)

# Display the result
print("Right-justified statement:", right_justified_statement, "|") # Added "|" to show the end
