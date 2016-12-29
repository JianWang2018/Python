# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.

# # key: can use lower() and isalnum()

import time

class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True

# other good solution:maxProfit
# key: can use map to build link of left and right node with maxDepth



def main():
    n="aaa aaa"
    time_t=time.time()
    sln=Solution().isPalindrome(n)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()