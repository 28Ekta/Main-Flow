# 16. Count Vowels and Consonants
# Objective: Count vowels and consonants.

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return f"The vowel in the string is {vowel_count}",f"The consonant in the string is {consonant_count}"

string =input("Enter Your String : ")
print(count_vowels_consonants(string))   