# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.

# key: from back to beginning, if 9, set 0 other wise +1 and return,
import time

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        digits=[1]+digits
        return digits



# other solution
class Solution1(object):

    def plusOne(self,digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]

def main():
    s=[9]*1000
    time_t=time.time()
    sln=Solution().plusOne(s)
    print(time.time()-time_t)
    time_t=time.time()
    sln=Solution1().plusOne(s)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()