import heapq
from math import floor

class MaxHeap:
    def __init__(self, arr):
        self.size = len(arr)
        self.heap = self.createHeap(arr)

    def createHeap(self, arr):
        last_non_leaf = floor(self.size / 2) - 1
        for i in reversed(range(0, last_non_leaf+1)):
            self.heapify(arr, i)
        return arr

    def heapify(self, arr, idx, limit=None):
        if not limit:
            limit = self.size
        while True:
            left = 2*idx + 1
            right = 2*idx + 2
            if idx >= limit or left >= limit or right >= limit:
                break
            largest = idx
            if arr[largest] < arr[left]:
                largest = left
            if arr[largest] < arr[right]:
                largest = right
            if largest != idx:
                arr[idx], arr[largest] = arr[largest], arr[idx]
                idx = largest

    def sort(self):
        arr = self.heap.copy()
        for i in reversed(range(1, self.size)):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, 0, i)
        return arr

    def dequeue(self):
        val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.size -= 1
        self.heapify(self.heap, 0)
        self.heap = self.heap[:-1]
        return val

    def enqueue(self, x):
        self.size += 1
        self.heap += [x]
        n = self.size - 1
        while n > 0 and self.heap[n // 2] < self.heap[n]:
            self.heap[n], self.heap[n // 2] = self.heap[n // 2], self.heap[n]
            n //= 2

##############################################################################

arr = [1, 3, 4, 6, 34, 2, 8]
heap = MaxHeap(arr)
print(heap.heap)
print(heap.sort())
print(heap.dequeue())
print(heap.heap)
print(heap.sort())
heap.enqueue(7)
print(heap.heap)
print(heap.sort())

##############################################################################

arr = [-a for a in arr]
heapq.heapify(arr)
heapq.heappop(arr)
heapq.heappush(arr, -7)
arr = [-a for a in arr]
print(arr)