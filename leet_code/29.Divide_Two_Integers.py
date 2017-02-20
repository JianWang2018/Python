# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
# key:This problem can be solved based on the fact that any number can be converted to the format of the following:
# num=a_0*2^0+a_1*2^1+a_2*2^2+...+a_n*2^n
# 基本思想就是把除数向左移位(×2)然后与被除数比较，直到发现仅次于被除数的那个值，减去该值后继续。也可以用递归做，这里图省事，就是一个循环了事。
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


#
# def main():
#     s=["[","]","(",")","["]
#     sln=Solution.isValid(s)
#     print(sln)
#
# if __name__=="__main__":
#     main()