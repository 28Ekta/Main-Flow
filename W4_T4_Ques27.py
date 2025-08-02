# W4_Task:4- 
# Ques:27. Longest Word in a Sentence

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


print(longest_word("Python is an amazing programming language"))