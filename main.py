from src import heap
import heapq

vals = list(range(1, 16)[::-1])
print(vals)
myheap = heap.Heap(vals)

print(myheap.getHeap())
myheap.replace(20)
print(myheap.getHeap())

myheap.replace(15)
print(myheap.getHeap())