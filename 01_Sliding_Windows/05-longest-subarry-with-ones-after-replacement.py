"""
Problem Statement 
Given an array containing 0s and 1s, if you are allowed to replace no more than
‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s
.
Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the "0" at index 5 and 8 to have the longest contiguous
subarray of 1s having length 6.
Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the "0" at index 6, 9, and 10 to have the longest
contiguous subarray of 1s having length 9.
"""
from typing import List


def length_of_longest_substring(arr: List[int], k: int) -> int:
    max_length = 0
    num_of_zero_in_window = 0
    window_start = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 0:
            num_of_zero_in_window += 1

        if num_of_zero_in_window > k:
            if arr[window_start] == 0:
                num_of_zero_in_window -= 1
            window_start += 1
        max_length = max(max_length, window_end-window_start+1)
    return max_length




def ans_length_of_longest_substring(arr, k):
    window_start = 0
    max_length = 0
    max_ones_count = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        if (window_end-window_start+1-max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(ans_length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(ans_length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


if __name__ == "__main__":
    main()

"""
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the count of numbers in the input array.
Space Complexity 
The algorithm runs in constant space O(1).
"""
