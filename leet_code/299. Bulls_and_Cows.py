# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
#
# For example:
#
# Secret number:  "1807"
# Friend's guess: "7810"
# Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".
#
# Please note that both secret number and friend's guess may contain duplicate digits, for example:
#
# Secret number:  "1123"
# Friend's guess: "0111"
# In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
# You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

# key: 1) use Counter to count guess and secret and sum their overlap. Then use zip to count A.
#2) dict in python can also use & it will return the elements with same key
from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)


#other solution:
#key: 1)The idea is simple, if two char is match, add aCnt, otherwise, record it and process bCnt in second pass.
#2) also make use of the string will only contains char of 0 to 9;
class Solution(object):
    def getHint(self, secret, guess):
        bull, cow = 0, 0
        s = {} # secret hashtable
        g = {} # guess hashtable

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1

        for k in s:
            if k in g:
                cow += min(s[k], g[k])

        return '{0}A{1}B'.format(bull, cow)







import time

def main():
    a="121234"
    b="123433"

    time_t=time.time()
    sln=Solution().getHint(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()