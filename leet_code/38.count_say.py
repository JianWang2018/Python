# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res ="1"
        for _ in range(n-1):
            temp=[]
            count =1
            for i in range(1,len(res)):
                if res[i]==res[i-1]:
                    count+=1
                else:
                    temp.append(str(count))
                    temp.append(res[i-1])
                    count=1
            temp.append(str(count))
            temp.append(res[-1])
            res=''.join(temp)
        return res


# other good solution

#Solution 1 ... using a regular expression

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s
#Solution 2 ... using a regular expression

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(group)) + digit
                    for group, digit in re.findall(r'((.)\2*)', s))
    return s
#Solution 3 ... using groupby

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
    return s

def main():
    n=10
    sln=Solution().countAndSay(n)
    print(sln)

if __name__=="__main__":
    main()