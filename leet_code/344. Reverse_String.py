# Write a function that takes a string as input and returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".

#key:1) chaneg the posiiton from beginning and end
class Solution(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)


#other solution:
#key: recursion and binary sort

class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])

#key: use the in built function
class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]


import time

def main():
    a=16
    time_t=time.time()
    sln=Solution().isPowerOfFour(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()