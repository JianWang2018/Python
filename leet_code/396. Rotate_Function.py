# Given an array of integers A and let n to be its length.
#
# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:
#
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
#
# Calculate the maximum value of F(0), F(1), ..., F(n-1).
#
# Note:
# n is guaranteed to be less than 105.
#
# Example:
#
# A = [4, 3, 2, 6]
#
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
#
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

# key: F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]
# F(k-1) = 0 * Bk-1[0] + 1 * Bk-1[1] + ... + (n-1) * Bk-1[n-1]
#        = 0 * Bk[1] + 1 * Bk[2] + ... + (n-2) * Bk[n-1] + (n-1) * Bk[0]
# Then,
#
# F(k) - F(k-1) = Bk[1] + Bk[2] + ... + Bk[n-1] + (1-n)Bk[0]
#               = (Bk[0] + ... + Bk[n-1]) - nBk[0]
#               = sum - nBk[0]
# Thus,
#
# F(k) = F(k-1) + sum - nBk[0]
# What is Bk[0]?
#
# k = 0; B[0] = A[0];
# k = 1; B[0] = A[len-1];
# k = 2; B[0] = A[len-2];
# ...

class Solution(object):
    """
    dictionary
    """
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        all_sum=0
        length=len(A)
        f=0
        for i in range(length):
            f+=i*A[i]
            all_sum+=A[i]

        max_=f
        for i in range(length-1,0,-1): # remember the -1 at the end of range if you want to loop from big to small
            f=f+all_sum-length*A[i]
            max_=max(f,max_)
        return max_





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