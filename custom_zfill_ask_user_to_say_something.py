def custom_zfill(input_string, length):

    if len(input_string) >= length:
        return input_string  # No padding needed

    padding_length = length - len(input_string)
    padding = "0" * padding_length
    return padding + input_string

