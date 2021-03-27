"""
Problem Statement
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:
Input: "Programming"
Output: "rrggmmPiano"
Explanation: "r", "g", and "m" appeared twice, so they need to appear before any
 other character.

Example 2:
Input: "abcbab"
Output: "bbbaac"
Explanation: "b" appeared three times, "a" appeared twice, and "c" appeared only
 once.
"""
from heapq import *


def sort_character_by_frequency_mine_solution(str):
    char_freq = {}
    # create a frequency table
    for char in str:
        char_freq[char] = char_freq.get(char, 0) + 1

    max_heap = []
    for char, freq in char_freq.items():
        heappush(max_heap, (-freq, char))

    out_str = ""
    while len(max_heap) != 0:
        freq, char = heappop(max_heap)
        freq = -freq
        out_str += char*freq
    return out_str


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency_mine_solution("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency_mine_solution("abcbab"))


if __name__ == "__main__":
    main()

"""
Time complexity 
The time complexity of the above algorithm is O(D*logD) where ‘D’ is the number of distinct characters in the input string. 
This means, in the worst case, when all characters are unique the time complexity of the algorithm will be O(N*logN) 
where ‘N’ is the total number of characters in the string.
Space complexity 
The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.
"""
