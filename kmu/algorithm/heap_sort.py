def maxHeapify(heap, heapSize, i):
    left = (i+1) * 2 - 1
    right = (i+1) * 2

    me = heap[i]
    largest = i

    # left vs largest
    if left < heapSize and heap[left] > heap[largest]:
        largest = left
    # right vs largest
    if right < heapSize and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[largest], heap[i] = heap[i], heap[largest]
        maxHeapify(heap, heapSize, largest)


def buildMaxHeap(array):
    leaf = int(len(array) / 2 - 1)
    for i in range(leaf, -1, -1):
        maxHeapify(array, len(array), i)


def heapSort(array):
    buildMaxHeap(array)
    heapSize = len(array)
    for i in range(heapSize-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapSize -= 1
        maxHeapify(array, heapSize, 0)


if __name__ == "__main__":
    array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    # maxHeapify(array, 3)
    # buildMaxHeap(array)
    heapSort(array)
    print(array)
