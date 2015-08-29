class Heap(object):
    def __init__(self):
        pass

    def getHeap(self):
        return self.internalheap

    def heapify(self, values):
        #no this technically works, but a really hacky implementation
        self.internalheap = values[:]
        for i in range(1, len(self.internalheap)):
            self.__heapify__(0)

    def __heapify__(self, idx):
        if len(self.internalheap)-1 < idx:
            return None
        curitem = self.internalheap[idx]
        leftidx = idx*2 + 1
        rightidx = idx*2 + 2
        left = self.__heapify__(leftidx)
        right = self.__heapify__(rightidx)



        if (curitem <= left or left == None) and (curitem <= right or right == None):
            return curitem
        elif left != None and left < curitem and (left < right or right == None):
            self.internalheap[idx], self.internalheap[leftidx] = self.internalheap[leftidx], self.internalheap[idx]
            return left
        else:
            self.internalheap[idx], self.internalheap[rightidx] = self.internalheap[rightidx], self.internalheap[idx]
            return right

        #0 - 0
        #1, 2 - 1
        #3, 4, 5, 6 - 2
        #7, 8, 9, 10, 11, 12, 13, 14 - 3


    def findMax(self):
        pass

    def findMin(self):
        pass

    def insert(self, item):
        pass

    def replace(self, item):
        pass