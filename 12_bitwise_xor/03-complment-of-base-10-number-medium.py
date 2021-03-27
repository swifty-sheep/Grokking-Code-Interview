"""
Problem Statement
Every non-negative integer N has a binary representation, for example, 8 can be
represented as “1000” in binary and 7 as “0111” in binary.

The complement of a binary representation is the number in binary that we get
when we change every 1 to a 0 and every 0 to a 1. For example, the binary
complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary
representation as a base-10 integer.

Example 1:
Input: 8
Output: 7
Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7
in base-10.

Example 2:
Input: 10
Output: 5
Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which is 5
in base-10.
"""


def calculate_bitwise_complement_mine_method(num):
    num_of_ones = 0
    ops = num
    while ops != 0:
        ops = ops >> 1
        num_of_ones += 1
    x = 2 ** num_of_ones - 1
    ans = num ^ x
    return ans


# ans
def calculate_bitwise_complement(num):
    # count number of total bits in `num`
    bit_count, n = 0, num
    while n > 0:
        bit_count += 1
        n = n >> 1

    all_bits_set = pow(2, bit_count)-1

    return num ^ all_bits_set


def main():
    print("Bitwise complement is: " + str(calculate_bitwise_complement_mine_method(8)))
    print("Bitwise complement is: " + str(calculate_bitwise_complement_mine_method(10)))


if __name__ == "__main__":
    main()

"""
Time Complexity 
Time complexity of this solution is O(b)O where ‘b’ is the number of bits 
required to store the given number.
Space Complexity 
Space complexity of this solution is O(1).
"""
