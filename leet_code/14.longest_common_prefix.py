
#Write a function to find the longest common prefix string amongst an array of strings.

# key use zip and set to verify if there is more than one value on each column, otherwise just return the min of strs

class Solution(object):

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        # if no return before, just return the min of strs
        return min(strs)
        