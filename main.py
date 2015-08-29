from src import heap
import heapq

vals = list(range(1, 16)[::-1])
print(vals)
myheap = heap.Heap()

myheap.heapify(vals)

print(myheap.getHeap())
#print(vals)
heapq.heapify(vals)
print(vals)