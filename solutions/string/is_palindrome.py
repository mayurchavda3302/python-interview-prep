"""

check if a string is a palindrome, considering only alphanumeric characters and ignoring cases.

example :
 mam is a palindrome, but "Hello" is not.
"""




# is palindrome using  string slicing
def is_palindrome_slicing(s)-> bool:

    return s == s[::-1]


def is_palindrome_two_pointer(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    left, right = 0, len(cleaned_s) - 1
    
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
        
    return True


# uinsg ragx -> no need to check the word just the chars
def is_palindrome_regex(s):
    import re
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    
    # it wii compare any of the it wii 
    return cleaned_s == cleaned_s[::-1]


new_string = "mam"
print(is_palindrome_slicing(new_string))  # Output: True