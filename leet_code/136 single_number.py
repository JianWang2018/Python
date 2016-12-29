3^0# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.

# # key: can use all xor to all the num, the xor of two same value is 0 and xor can change order

import time

class Solution(object):
    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

# other good solution:maxProfit

def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key


def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)

def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)

def singleNumber(self, nums):
    return reduce(operator.xor, nums)


def main():
    n=[1,1,2,2,3,4,4]
    time_t=time.time()
    sln=Solution().singleNumber2(n)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()