# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.


# key:The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

class Solution(object):
    def myAtoi(self, s):
        if len(s)==0: return 0
        ls=list(s.strip())

        sign=-1 if ls[0]=="-" else 1
        if ls[0] in ["-","+"] : del ls[0] # should delete the sign

        res,i=0,0
        while i<len(ls) and ls[i].isdigit():
            res=res*10+ord(ls[i])-ord("0")
            i+=1
        return max(-2**31,min(sign*res,2**31-1))



def main():
    s="   +123"
    sln=Solution().myAtoi(s)
    print(sln)

if __name__=="__main__":
    main()