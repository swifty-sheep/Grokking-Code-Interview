"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than
 K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is
"araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is
"aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters
are "cbbeb" & "bbebi".
"""


def longest_substring_with_k_distinct(str1: str, k: int) -> int:
    max_length = 0
    window_start = 0
    char_freq = {}

    for window_end in range(len(str1)):
        if str1[window_end] not in char_freq:
            char_freq[str1[window_end]] = 0
        char_freq[str1[window_end]] += 1

        while len(char_freq) > k:
            left_char = str1[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1

        # remember max length so far
        max_length = max(max_length, window_end-window_start+1)
    return max_length


def main():
    print("Length of the longest substring: " + str(
        longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(
        longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(
        longest_substring_with_k_distinct("cbbebi", 3)))


if __name__ == "__main__":
    main()


"""
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string. 
The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).
Space Complexity 
The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
"""
