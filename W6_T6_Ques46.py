
# W6_Task:6- 
# Ques: 46. Word Ladder Problem

from collections import deque
def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + c + word[i+1:]
                if newWord in wordSet:
                    wordSet.remove(newWord)
                    queue.append((newWord, steps + 1))
    return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(word_ladder(beginWord, endWord, wordList))  