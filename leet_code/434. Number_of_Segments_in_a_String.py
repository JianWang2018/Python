# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5
#key:1) current is space and previous is not space
#2) should add a space at the end of the string
import collections
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s+" "
        print(s)
        res=0
        for i in range(1,len(s)):
            if s[i]==" " and s[i-1]!=" ":
                res+=1
        return res






#other solution
# key: can use split
class Solution(object):
def countSegments(self, s):
"""
:type s: str
:rtype: int
"""
return len(s.split())
import time

def main():
    a="220"
    b="11"
    time_t=time.time()
    sln=Solution().addStrings(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()