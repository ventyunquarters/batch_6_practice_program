def alternate_rsuffix(input_string, suffix):
    if len(suffix) > len(input_string):
        return input_string
    if input_string[-len(suffix):] == suffix:
        return input_string[:-len(suffix)]
    else:
        return input_string

# Ask user for a python file name
python_file = input("Enter a Python file name (e.g., my_script.py): ")

# Remove the .py suffix if present
cleaned_file = alternate_rsuffix(python_file, ".py")

# Display the result
print("File name without .py extension:", cleaned_file)