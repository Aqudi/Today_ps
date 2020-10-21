def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break


def bucketSort(arr):
    bucket = [[] for i in arr]

    n = len(arr)
    for i in range(1, n):
        idx = arr[i] % n
        bucket[idx].append(arr[i]);

    arr.clear()
    for i in range(n):
        insertionSort(bucket[i])
        arr += bucket[i]


if __name__ == "__main__":
    arr = [23, 45, 12, 45, 23, 12, 45, 23, 57, 324, 98]
    bucketSort(arr)
    print(arr)
