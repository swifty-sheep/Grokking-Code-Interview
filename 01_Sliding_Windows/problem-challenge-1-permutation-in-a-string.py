"""
Problem Challenge 1
Permutation in a String (hard) 
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.
Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


def find_permutation(str1: str, pattern: str):
    window_start = 0
    matched = 0
    char_freq = {}
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    # goal - match all characters from `char_freq` with current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1

        if matched == len(char_freq):
            return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1
    return False


def main():
    print("Permutation exist: " + str(find_permutation("oidbcaf", "abc")))
    print("Permutation exist: " + str(find_permutation("odicf", "dc")))
    print(
        "Permutation exist: " + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print("Permutation exist: " + str(find_permutation("aaacb", "abc")))


if __name__ == "__main__":
    main()

"""
Time Complexity #
The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ 
are the number of characters in the input string and the pattern respectively.

Space Complexity #
The space complexity of the algorithm is O(M) since in the worst case, 
the whole pattern can have distinct characters which will go into the HashMap.
"""
