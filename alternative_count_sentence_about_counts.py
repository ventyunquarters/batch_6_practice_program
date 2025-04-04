def custom_count(input_string, substring):
    count = 0
    i = 0
    while i <= len(input_string) - len(substring):
        if input_string[i:i + len(substring)] == substring:
            count += 1  # Increment the count
            i += len(substring)
        else:
            i += 1
    return count

# Ask user to enter a sentence about cats
sentence = input("Enter a sentence about cats: ")

# Count how many times "cats" appears (case-sensitive)
cats_count = custom_count(sentence, "cats")

# Display the result
print(f"The substring 'cats' appears {cats_count} times in your sentence.")