# def longest_palindrome(st):
#     if st==st[::-1]:
#         return st  #string itself is a palindrome
#     else:
#         n=len(st)
#         cur=''
#         palins=[]
#         # Generating all possible palindromes of length 2 or more
#         for i in range(n):
#             cur+=st[i]
#             for j in range(i+1, n):
#                 cur+=st[j]
#                 if cur==cur[::-1]:
#                     palins.append(cur)
#             cur=''
#         print(palins)
#         # Getting max length and index of it
#         max_length = 0
#         ind = 0
#         for index,s in enumerate(palins):
#             # >= will give the index of largest palin that comes last in the list
#             if len(s)>max_length:
#                 max_length=len(s)
#                 ind = index
#         # This will return the Value with large that comes first in the list
#         if max_length!=0:
#             return palins[ind]
#         else: 
#             return -1
    
def longestPalindrome(s):
    def expandAroundCenter(s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if not s or len(s) == 0:
        return ""
    
    longest = ""
    for i in range(len(s)):
        # Check for odd length palindromes
        odd_palindrome = expandAroundCenter(s, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Check for even length palindromes
        even_palindrome = expandAroundCenter(s, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest
    
s1 = "babad"
print(longestPalindrome(s1)) 

