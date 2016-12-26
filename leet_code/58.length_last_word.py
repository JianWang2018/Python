# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.

# key: start from the back to forward, and first remove the blank at the end
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # remove the blank from the end
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                break

        res=0
        for j in range(i,-1,-1):
            if s[j]!=" ":
                res+=1
            else:
                break
        return res







# other good solution
def lengthOfLastWord(self, s):
    return len(s.rstrip(' ').split(' ')[-1])

def main():
    s="hello world a a "
    sln=Solution().lengthOfLastWord(s)
    print(sln)

if __name__=="__main__":
    main()