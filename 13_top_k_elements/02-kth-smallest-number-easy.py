"""
Problem Statement
Given an unsorted array of numbers, find Kth smallest number in it.
Please note that it is the Kth smallest number in the sorted order, not the Kth
distinct element.
Note: For a detailed discussion about different approaches to solve this
problem, take a look at Kth Smallest Number.

Example 1:
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is "5", as the first two smaller numbers
are [1, 2].

Example 2:
Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is "5", as the first three small numbers
are [1, 2, 5].

Example 3:
Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is "11", as the first two small numbers
are [5, -1].
"""
from heapq import *


def find_Kth_smallest_number(nums, k):
    min_heap = []
    for i in range(len(nums)):
        heappush(min_heap, nums[i])
    kth_smallest = -1
    for i in range(k):
        kth_smallest = heappop(min_heap)
    if kth_smallest == -1:
        return None
    return kth_smallest


def find_kth_smallest_number(nums, k):
    max_heap = []
    # put first k numbers in the max heap
    for i in range(k):
        heappush(max_heap, -nums[i])
    # go through the remaining numbers of the array, if the number from the
    # array is smaller than the top(biggest) number of the heap, remove the top
    # number from heap and add the number from array
    for i in range(k, len(nums)):
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    # the root of the hap has the kth smallest number
    return -max_heap[0]


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a "5"
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))

    print("Kth smallest number is: " +
          str(find_kth_smallest_number([5, 12, 11, -1, 12], 3)))


if __name__ == "__main__":
    main()

"""
Time complexity 
The time complexity of this algorithm is O(K*logK+(N-K)*logK), which is asymptotically equal to O(N*logK)
Space complexity 
The space complexity will be O(K) because we need to store ‘K’ smallest numbers in the heap.
An Alternate Approach 
Alternatively, we can use a Min Heap to find the Kth smallest number. 
We can insert all the numbers in the min-heap and then extract the top ‘K’ numbers from the heap to find the Kth smallest number. 
Initializing the min-heap with all numbers will take O(N) and extracting ‘K’ numbers will take O(KlogN). 
Overall, the time complexity of this algorithm will be O(N+KlogN) and the space complexity will be O(N).
"""
