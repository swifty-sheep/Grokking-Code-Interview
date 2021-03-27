"""
Problem Statement
Design a class to efficiently find the Kth largest element in a stream of
numbers.

The class should have the following two things:
The constructor of the class should accept an integer array containing initial
numbers from the stream and an integer ‘K’.
The class should expose a function add(int num) which will store the given
number and return the Kth largest number.

Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return "5".
2. Calling add(13) should return "6".
2. Calling add(4) should still return "6".
"""
from heapq import *
from typing import List


class KthLargestNumberInStream:

    def __init__(self, arr: List[int], k: int):
        self.min_heap = []
        self.k = k
        for num in arr:
            self.add(num)

    def add(self, num: int):
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                heappop(self.min_heap)
                heappush(self.min_heap, num)
        return self.min_heap[0]


def main():
    kth_largest_number = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kth_largest_number.add(6)))
    print("4th largest number is: " + str(kth_largest_number.add(13)))
    print("4th largest number is: " + str(kth_largest_number.add(4)))


if __name__ == "__main__":
    main()

"""
Time complexity 
The time complexity of the add() function will be O(logK) since we are inserting the new number in the heap.
Space complexity 
The space complexity will be O(K) for storing numbers in the heap.
"""
