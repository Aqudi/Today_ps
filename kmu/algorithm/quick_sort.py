
import pdb


def partition(arr, p, r):
    pivot = arr[r]

    idx = p
    for i in range(p, r):
        if arr[i] <= pivot:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1
    arr[idx], arr[r] = arr[r], arr[idx]
    return idx


def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)


if __name__ == "__main__":
    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    quickSort(arr, 0, len(arr)-1)
    print(arr)
