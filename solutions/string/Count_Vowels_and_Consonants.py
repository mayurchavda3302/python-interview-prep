"""


"""



def count_vowels_and_consonants(s):
    """
    Count the number of vowels and consonants in a given string.

    Args:
        s (str): The input string.

    """
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():  # Check if the character is an alphabet
            # uisng in oprator
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count




# Example usage
input_string = "Hello World!"
vowels, consonants = count_vowels_and_consonants(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")