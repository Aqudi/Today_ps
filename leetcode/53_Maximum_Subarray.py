import sys
from typing import List


class Solution:
    def findMaxSubArray(self, nums, low, high):
        if high == low:
            return (low, high, nums[low])

        mid = int((low + high) / 2)

        li, lj, ls = self.findMaxSubArray(nums, low, mid)
        ri, rj, rs = self.findMaxSubArray(nums, mid+1, high)
        ci, cj, cs = self.findMaxCrossSubArray(nums, low, mid, high)

        if ls >= rs and ls >= cs:
            return (li, lj, ls)
        elif rs >= ls and rs >= cs:
            return (ri, rj, rs)
        else:
            return (ci, cj, cs)

    def findMaxCrossSubArray(self, nums, low, mid, high):
        ls = -sys.maxsize
        rs = -sys.maxsize

        ml = 0
        mr = 0

        s = 0
        for i in range(mid, low-1, -1):
            s += nums[i]
            if s > ls:
                ls = s
                ml = i
        s = 0
        for i in range(mid+1, high+1):
            s += nums[i]
            if s > rs:
                rs = s
                mr = i
        return (ml, mr, ls + rs)

    def maxSubArray(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        i, j, s = self.findMaxSubArray(nums, 0, high)
        return s


if __name__ == "__main__":
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))
