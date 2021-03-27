"""
Problem Statement
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""


def pair_with_target_sum(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1
    return [-1, -1]


def main():
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))


if __name__ == "__main__":
    main()

"""
Time Complexity 
The time complexity of the above algorithm will be O(N), 
where ‘N’ is the total number of elements in the given array.
Space Complexity 
The algorithm runs in constant space O(1).
An Alternate approach 
Instead of using a two-pointer or a binary search approach, 
we can utilize a HashTable to search for the required pair. 
We can iterate through the array one number at a time. 
Let’s say during our iteration we are at number ‘X’, 
so we need to find ‘Y’ such that “X + Y == TargetX+Y==Target”. 
We will do two things here:
Search for ‘Y’ (which is equivalent to “Target - XTarget−X”) in the HashTable. 
If it is there, we have found the required pair.
Otherwise, insert “X” in the HashTable, so that we can search it for the later numbers.
Here is what our algorithm will look like:
"""


def pair_with_target_sum_using_hashtable(arr, target_sum):
    nums = {}  # to store numbers and their indices
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]


def main():
    print(pair_with_target_sum_using_hashtable([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum_using_hashtable([2, 5, 9, 11], 11))


main()

"""
Time Complexity 
The time complexity of the above algorithm will be O(N), 
where ‘N’ is the total number of elements in the given array.
Space Complexity 
The space complexity will also be O(N), as, in the worst case, we will be pushing ‘N’ numbers in the HashTable.
"""
