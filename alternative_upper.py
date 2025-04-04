#Define custom upper
def custom_upper(input_string):

#Use arg input string to convert and return uppercase version
    result = ""
    for char in input_string:
        if 'a' <= char < 'z':
            #Convert lowerase to upper using ASCII values
            result += chr(ord(char) - 32)
        else:
            result += char
    return result
#Ask user to input a statement
user_statement = input("Enter a statement: ")
#Convert to uppercase
uppercase_statement = custom_upper(user_statement)
#Display with result
print("Uppercase statement:", uppercase_statement)
