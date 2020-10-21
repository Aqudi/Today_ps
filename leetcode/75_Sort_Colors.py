from typing import List


class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break

    def bucketSort(self, arr):
        n = len(arr) + 1

        bucket = [[] for i in range(n)]

        for i in arr:
            idx = i % n
            bucket[idx].append(i)

        arr.clear()
        for i in range(n):
            self.insertionSort(bucket[i])
            arr += bucket[i]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.bucketSort(nums)
