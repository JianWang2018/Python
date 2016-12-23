# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


# key: use dictionary to store pair of parentheses, when char is in keys, append to stack, else to test if the pop of stack will
# construct a parentheses.
class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


def main():
    s=["[","]","(",")","["]
    sln=Solution.isValid(s)
    print(sln)

if __name__=="__main__":
    main()