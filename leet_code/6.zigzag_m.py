# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

# key: build number of rows blank string,put the character to the corresponding rows,change the direction when index equal to 0 or num_rows-1


class Solution(object):
    def convert(self, s, numRows):
        step = (numRows == 1 or numRows >= len(s)) - 1  # 0 or -1
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows-1:
                step = -step  #change direction
            idx += step
        return ''.join(rows)
