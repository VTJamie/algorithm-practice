from src import heap
import heapq

vals = list(range(1, 7)[::-1])
myheap = heap.Heap()

myheap.heapify(vals)

print(myheap.getHeap())
print(vals)
heapq.heapify(vals)
print(vals)