import heapq
class DataStream:
    def __init__(self):
        self.min_heap = [] 
        self.max_heap = [] #max_heap would be multiplied by -1
    
    #Adds the 'num' to appropriate heap
    def add(self, num:int) -> None:
        heapq.heappush(self.max_heap, -1 * num)

        if (self.max_heap and self.min_heap and (-1 * self.max_heap[0]) > self.min_heap[0]):
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * val)

    #Finding the median
    def get_median(self) -> float:
        #If min_heap has more element
        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        #If min_heap has more elements,
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        
        #If they are the same length, find the average
        return (-1 * self.max_heap[0] + self.min_heap[0]) / 2

obj = DataStream()
numbers = [4, 1, 3, 9, 2, 11, 14, 5]
for num in numbers:
    obj.add(num)
    median = obj.get_median()
    print(median, end=", ")

