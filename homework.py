def reverseString(s):
    # Base case: if the string is empty or has one character
    # Generalized form: reverse the rest of the string and append the first character

def isPalindrome(s):
    # Base case: if the string is empty or has one character, it's a palindrome
    # Generalized form: compare the first and last characters, and recurse on the middle substring

def string_length(s):
    # Base case: an empty string has a length of 0
    # Generalized form: 1 (for the current character) + length of the remaining string

def remove_character(s, char):
    # Base case: if the string is empty, return an empty string
    # Generalized form: if the current character matches, skip it; otherwise, include it


# Test Reverse String
print("Test Reverse String")
assert reverseString('yoonha') == 'ahnooy', "Test Case 1 Failed"
assert reverseString('') == '', "Test Case 2 Failed"  # Empty string
assert reverseString('a') == 'a', "Test Case 3 Failed"  # Single character
assert reverseString('abcde') == 'edcba', "Test Case 4 Failed"  # Odd-length string
assert reverseString('abcdef') == 'fedcba', "Test Case 5 Failed"  # Even-length string
print("All Reverse String Test Cases Passed!")

# Test Is Palindrome
print("\nTest Is Palindrome")
assert isPalindrome('racecar') == True, "Test Case 1 Failed"  # Palindrome
assert isPalindrome('hello') == False, "Test Case 2 Failed"  # Not a palindrome
assert isPalindrome('') == True, "Test Case 3 Failed"  # Empty string is a palindrome
assert isPalindrome('a') == True, "Test Case 4 Failed"  # Single character
assert isPalindrome('abba') == True, "Test Case 5 Failed"  # Even-length palindrome
assert isPalindrome('abcba') == True, "Test Case 6 Failed"  # Odd-length palindrome
assert isPalindrome('abca') == False, "Test Case 7 Failed"  # Close but not a palindrome
print("All Palindrome Test Cases Passed!")

# Test String Length
print("\nTest String Length")
assert string_length('hello') == 5, "Test Case 1 Failed"
assert string_length('') == 0, "Test Case 2 Failed"  # Empty string
assert string_length('a') == 1, "Test Case 3 Failed"  # Single character
assert string_length('abcdef') == 6, "Test Case 4 Failed"
assert string_length(' ') == 1, "Test Case 5 Failed"  # Single space
assert string_length('12345') == 5, "Test Case 6 Failed"  # String of numbers
print("All String Length Test Cases Passed!")

# Test Remove Character
print("\nTest Remove Character")
assert remove_character('hello world', 'l') == 'heo word', "Test Case 1 Failed"
assert remove_character('apple', 'p') == 'ale', "Test Case 2 Failed"
assert remove_character('', 'a') == '', "Test Case 3 Failed"  # Empty string
assert remove_character('aaaaa', 'a') == '', "Test Case 4 Failed"  # All characters removed
assert remove_character('banana', 'n') == 'baaa', "Test Case 5 Failed"
assert remove_character('cherry', 'z') == 'cherry', "Test Case 6 Failed"  # Character not present
assert remove_character('abcabcabc', 'b') == 'acacac', "Test Case 7 Failed"
assert remove_character('111223311', '1') == '2233', "Test Case 8 Failed"  # Numeric string
print("All Remove Character Test Cases Passed!")
