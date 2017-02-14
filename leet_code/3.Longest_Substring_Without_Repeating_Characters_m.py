# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# key: can use divmod to find sum and carry 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        my_dict,start,max_len={},0,0
        for i, element in enumerate(s):
            # if the element has occur before
            if element in my_dict:
                max_len=max(max_len,i-start)
                start=max(start,my_dict[element]+1)

            my_dict[element]=i
        return max(max_len,len(s)-start)