def custom_zfill(input_string, length):

    if len(input_string) >= length:
        return input_string  # No padding needed

    padding_length = length - len(input_string)
    padding = "0" * padding_length
    return padding + input_string

# Ask user to say something
user_input = input("Say something: ")
desired_length = int(input("Enter the desired length (with leading zeros): "))

# Pad the string with leading zeros
zero_filled_string = custom_zfill(user_input, desired_length)

# Display the result
print("Zero-filled string:", zero_filled_string)