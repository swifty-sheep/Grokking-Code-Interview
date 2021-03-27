"""
Problem Statement 
Given an unsorted array of numbers, find the top ‘K’ frequently occurring
numbers in it.

Example 1:
Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both "11" and "12" appeared twice.

Example 2:
Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only "11" appeared twice, all other numbers appeared once.
"""
from heapq import *


def find_k_frequent_numbers_mine_method(nums, k):
    max_heap = []
    num_freq = {}
    for num in nums:
        if num not in num_freq:
            num_freq[num] = 0
        num_freq[num] += 1
    print(num_freq)
    num_set = list(set(nums))
    for i in range(k):
        heappush(max_heap, (num_freq[num_set[i]], num_set[i]))
    for i in range(k, len(num_set)):
        num = num_set[i]
        if num_freq[num] > max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap, (num_freq[num], num))
    result = []
    for num in max_heap:
        result.append(num[1])
    return result


def find_k_frequent_numbers(nums, k):
    # find the frequency of each number
    num_freq = {}
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1
    min_heap = []

    # go through all nums of the num_freq and push them in the min_heap, which
    # will have top k freq numbers. It the heap size is more than k, remove the
    # smallest (top) number
    for num, freq in num_freq.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)

    # create a list of top k numbers
    top_numbers = []
    while min_heap:
        top_numbers.append(heappop(min_heap)[1])
    return top_numbers


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers_mine_method([1, 3, 5, 12, 11, 12, 11],
                                                  2)))
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers_mine_method([5, 12, 11, 3, 11], 2)))
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


if __name__ == "__main__":
    main()

"""
Time complexity 
The time complexity of the above algorithm is O(N+N*logK).
Space complexity 
The space complexity will be O(N). Even though we are storing only ‘K’ numbers in the heap. 
For the frequency map, however, we need to store all the ‘N’ numbers.
"""
