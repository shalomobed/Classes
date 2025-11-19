import heapq
import math

class Percentile75Monitor:
    def __init__(self):
        self.lower = [] #max-heap
        self.upper = [] #min-heap
        self.count = 0

    def add(self, num):

        #Choose the correct heap to insert to
        if not self.lower or num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)

        self.count += 1
        
        #Finding the 75th percentile
        desired_lower_size = math.ceil(0.75 * self.count)

        while len(self.lower) > desired_lower_size:
            moved = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, moved)

        while len(self.lower) < desired_lower_size and self.upper:
            moved = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -moved)

    def get_75th(self):
        if not self.lower:
            return None
        return -self.lower[0]

#Sample Input
monitor = Percentile75Monitor()
nums = list(map(int, input("Enter numbers:").split(",")))

for n in nums:
    monitor.add(n)

print(monitor.get_75th())