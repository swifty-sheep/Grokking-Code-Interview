"""
Problem Statement
Given a list of non-overlapping intervals sorted by their start time, insert a
given interval at the correct position and merge all necessary intervals to
produce a list that has only mutually exclusive intervals.

Example 1:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them
into one [4,7].

Example 2:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we
merged them into [4,12].

Example 3:
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them
into one [1,4].
"""
from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]):
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]

    result = []
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            result.append([start, end])
            start = interval[0]
            end = interval[1]
    result.append([start, end])
    return result


def insert_ans(intervals: List[List[int]], new_interval: List[int]):
    merged = []
    i, start, end = 0, 0, 1
    # skip (and add to merged) all intervals that come before the "new_interval"
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1
    
    # merge all intervals that overlap with "new_interval"
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1
    merged.append(new_interval)
    # add all remaining intervals to the merged
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


def main():
    print("Intervals after inserting the new interval: " + str(
        insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(
        insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(
        insert([[2, 3], [5, 7]], [1, 4])))

    print("Intervals after inserting the new interval: " + str(
        insert_ans([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(
        insert_ans([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(
        insert_ans([[2, 3], [5, 7]], [1, 4])))


if __name__ == "__main__":
    main()

"""
Time complexity 
As we are iterating through all the intervals only once, the time complexity of the above algorithm is O(N)O, 
where ‘N’ is the total number of intervals.
Space complexity 
The space complexity of the above algorithm will be O(N) as we need to return a list containing all the merged intervals.
"""
