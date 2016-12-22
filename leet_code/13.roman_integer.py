# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
class Solution(object):
    def romanToInt(self, s):

        roman = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}

        prev = result =0

        for i in range(len(s)-1, -1, -1):
            cur = roman[s[i]]
            if cur < prev:
                result -= cur
            else:
                result += cur
            prev = cur

        return result