# W6_Task:6- 
# Ques: 40. Word Frequency in Text

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
text = "Hello world hello ekta ekta"
print(word_frequency(text))  