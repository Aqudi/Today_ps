"""
Radix Sort
Counting sort를 1의 자리부터 n의 자리까지 반복해서 수행

Stable sort
"""

BASE = 16


def getHexIdx(num, i):
    h = hex(num)
    s = len(h) - 1
    return int(h[s-i], 16)


def countingSort16(arr, k):
    c = [0 for i in range(BASE)]

    for i in range(len(arr)):
        c[getHexIdx(arr[i], k)] += 1

    for i in range(1, len(c)-1):
        c[i] = c[i] + c[i-1]

    b = [-1 for i in arr]
    for i in range(len(arr)-1, -1, -1):
        cnum = getHexIdx(arr[i], k)
        b[c[cnum]-1] = arr[i]
        c[cnum] -= 1
    return b


def radixSort16(arr):
    # int범위내의 입력이므로 2^32까지 커버
    for i in range(8):
        arr = countingSort16(arr, i)
    return arr


if __name__ == "__main__":
    arr = [23, 45, 55, 26, 33, 56, 25, 66, 34, 88, 90, 112, 45]
    arr = radixSort16(arr)
    print(arr)
