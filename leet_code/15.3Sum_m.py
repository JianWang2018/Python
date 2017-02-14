# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def intToRoman(self, num):
       #roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        if (num<1 or num>3999): return ''
        roman=["M","CM","D","CD","C","XC","L",'XL',"X","IX",'V',"IV","I"]
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i=0
        res=[]

        while (num>0):
            while(num>=values[i]):
                num-=values[i]
                res.append(roman[i])
            i+=1
        return res


class Solution1(object):
    def intToRoman(self, num):
       #roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        thousand=["","M",'MM','MMM']
        hundred=["",'C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        ten=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        one=['','I','II','III','IV','V','VI','VII','VIII','IX']
        r_string=''+thousand[num//1000]+hundred[num%1000//100]+ten[num%100//10]+one[num%10]
        return r_string


#
# def main():
#     s="   +123"
#     sln=Solution().myAtoi(s)
#     print(sln)
#
# if __name__=="__main__":
#     main()