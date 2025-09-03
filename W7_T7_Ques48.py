# W7_Task:7- 
# Ques:48. Longest Palindromic Substring
def longest_palindrome(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    longest = ""
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i+1)
        longest = max(longest, odd, even, key=len)
    return longest

print(longest_palindrome("babad"))  


