
#check Palindrome
#Palindrome is a string or text(a word) if we read from Left and Right 
# it should be equal like: (aabaa)  (lool)
# There, I just checked s is equal to its reverse(s[::-1 means reverse of s]

def solution(s):
    return s == s[::-1]
