class Heap(object):
    def __init__(self, values):
        self.internalheap = values[:]
        self.heapify()

    def getHeap(self):
        return self.internalheap

    def heapify(self):
        #no this technically works, but a really hacky implementation

        self.comparisons = 0
        for i in range(0, len(self.internalheap))[::-1]:
            self.__heapify__(i)

        print("Comparisons {}".format(self.comparisons))

    def __heapify__(self, idx):
        leftidx = idx*2 + 1
        rightidx = idx*2 + 2
        left = self.internalheap[leftidx] if leftidx < len(self.internalheap) else None
        right = self.internalheap[rightidx] if rightidx < len(self.internalheap) else None
        largest = idx

        if left != None:
            self.comparisons += 1

        if right != None:
            self.comparisons += 1

        if left != None and left < self.internalheap[largest]:
            largest = leftidx

        if right != None and right < self.internalheap[largest]:
            largest = rightidx

        if largest != idx:
            print("Swapping {} with {}".format(self.internalheap[idx], self.internalheap[largest]))
            self.internalheap[idx], self.internalheap[largest] = self.internalheap[largest], self.internalheap[idx]
            self.__heapify__(largest)


    def findMin(self):
        return self.internalheap[0] if len(self.internalheap) > 0 else None

    def insert(self, item):
        self.internalheap.append(item)
        self.heapify()

    def replace(self, item):
        if len(self.internalheap) > 0:
            self.internalheap[0] = item
            self.__heapify__(0)