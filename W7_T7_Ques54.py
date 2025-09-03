# W7_Task:7- 
# Ques:54. Palindrome Partitioning
def partition(s):
    result = []

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start+1, len(s)+1):
            if s[start:end] == s[start:end][::-1]:
                backtrack(end, path+[s[start:end]])

    backtrack(0, [])
    return result


print(partition("aab")) 
