# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# key: The idea is intuitive. Use two integers to count the remaining left parenthesis (n) and the right
# parenthesis (m) to be added. At each function call add a left parenthesis if n >0 and add a right parenthesis if m>0. Append the result and terminate recursive calls when both m and n are zero.
class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        def gen_parent(p, left, right, res=[]):
            if left:
                gen_parent(p + '(', left-1, right)
            if right > left:
                gen_parent(p + ')', left, right-1)
            if not right:
                res += p,
            return res
        return gen_parent('', n, n)



#
# def main():
#     s="   +123"
#     sln=Solution().myAtoi(s)
#     print(sln)
#
# if __name__=="__main__":
#     main()