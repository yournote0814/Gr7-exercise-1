"""
Exercise 3

# A program for you calculate the length of a string.
#  A program count the number of characters in a string.
#  A program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#  A program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces
# Using + Concatenate Strings in Python get two strings from user input and concatenate them
# Using + Concatenate in Python using your name and your age in a paragraph

"""

# A program to calculate the length of a string
def calculate_length(s):
    return len(s)

# A program to count the number of characters in a string
def count_characters(s):
    return len(s)

# A program to get a string where all occurrences of its first char have been changed to '$', except the first char itself
def replace_first_char(s):
    if len(s) == 0:
        return s
    first_char = s[0]
    modified_string = first_char + s[1:].replace(first_char, '$')
    return modified_string

# A program to get a single string from two given strings, separated by a space and swap the first two characters of each string
def swap_first_two_chars(s1, s2):
    if len(s1) < 2 or len(s2) < 2:
        return "Strings are too short to swap characters."
    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]
    return new_s1 + " " + new_s2

# Concatenate Strings in Python using 4 variables and concatenate them with spaces
def concatenate_with_spaces(a, b, c, d):
    return a + " " + b + " " + c + " " + d

# Concatenate Strings in Python by getting two strings from user input and concatenating them
def user_concatenate():
    str1 = input("Enter First Name: ")
    str2 = input("Enter Last Name: ")
    return str1 + " " + str2

# Concatenate strings in Python using your name and age in a paragraph
def name_and_age_paragraph(name, age):
    return f"My name is {name} and I am {age} years old."

# Main function to demonstrate the program
if __name__ == "__main__":
    # Demonstrating the length calculation
    string_example = "hello world"
    
    print("Example String : ",string_example)
    print("Length of the string:", calculate_length(string_example))
 
    # Demonstrating the character count
    print("Number of characters in the string:", count_characters(string_example))
    
    
    # Demonstrating the replace first char
    string_with_replacement = "restart"
    
    print("Example String : ",string_with_replacement)
    print("Modified string:", replace_first_char(string_with_replacement))
    print("")
    
    # Demonstrating the swap first two characters
    swap1 = "abc"
    swap2 = "xyz"
    
    print("Example String : ", swap1 + " " + swap2)
    print("Swapped strings:", swap_first_two_chars(swap1, swap2))
    
    
    # Demonstrating concatenation with spaces
    print("Concatenated string with spaces:", concatenate_with_spaces("Hello", "world", "this", "works"))
    
    
    # Demonstrating user input concatenation
    print("Concatenated user input:", user_concatenate())
    print("")
    
    # Demonstrating name and age paragraph
    print(name_and_age_paragraph("Ryan", 23))
