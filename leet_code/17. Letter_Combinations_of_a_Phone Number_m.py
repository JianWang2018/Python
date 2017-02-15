# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# key: use recursion add digit[0] and digit[1:]

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #define the dictionary for the 0-9 numbers
        my_dic={}
        my_dic["0"]=[" "]
        my_dic["1"]=["*"]
        my_dic["2"]=["a","b",'c']
        my_dic['3']=['d','e','f']
        my_dic['4']=['g','h','i']
        my_dic['5']=['j','k','l']
        my_dic['6']=['m','n','o']
        my_dic['7']=['p','q','r','s']
        my_dic['8']=['t','u','v']
        my_dic['9']=['w','x','y','z']

        if len(digits)==0:
            return []

        if len(digits)==1:
            return my_dic[digits[0]]

        cur=my_dic[digits[0]]
        later=self.letterCombinations(digits[1:])

        return ([x+y for x in cur for y in later])



#
# def main():
#     s="   +123"
#     sln=Solution().myAtoi(s)
#     print(sln)
#
# if __name__=="__main__":
#     main()