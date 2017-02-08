# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
#
# Each LED represents a zero or one, with the least significant bit on the right.
#
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
#
# Example:
#
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

#key:To make the problem much much more easier, I divide the problem into 3 parts:

# calculate how many digits the number has.
# calculate what the muber is.
# find out which digit in the number is we want.
# You can find the relative code part in the code section.
# Here is an example to help you to understand my code:
#
# Example:
#
# Input: 250
#
# After step 1, you will find that the 250th digit must belong to a 3-digit number, since 1~9 can only provide 9 digits and 10~99 can only provide 180 digits. Here, n = 250 - 9 - 90 * 2 = 61, and digits = 3.
#
# In step 2, we will find the target number, which named as number in my code. From step 1, the n becomes to 61, which means "the 61st digit in 3-digit number is the digit we are looking for ." Easily, we know the 61st digit in 3-digit number belongs to number = 100 + 61 / 3 = 100 + 20 = 120. index is the index of the target digit in number. If index equals to 0, it means the target digit is the last digit of number.
#
# Step 3, from step 2, we know index = n % digits = 61 % 3 = 1, which means the target digit is the 1st digit in number. Then, return 1.


#key: 1)Just go through the possible times and collect those with the correct number of one-bits.
#2) transport to binary and each 1 represent a light led
def readBinaryWatch(self, num):
    return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]






#other solution
class Solution1(object):
    def maxRotateFunction(self, A):
        s = 0; n = len(A)
        for i in range(n):
            s += i*A[i]
        sumA = sum(A); m = s
        for num in A:
            s += n*num - sumA
            m = max(m, s)
        return m

import time

def main():
    a=[4,3,2,6]
    time_t=time.time()
    sln=Solution().maxRotateFunction(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()