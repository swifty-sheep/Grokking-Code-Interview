"""
Problem Challenge 1
Palindrome LinkedList (medium)
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.
Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head: Node):
    if head is None or head.next is None:
        return True

    mid_point = find_mid_point(head=head)
    head_of_second_half = reverse(mid_point)
    copied_second = head_of_second_half

    curr = head
    while curr and head_of_second_half:
        if curr.value != head_of_second_half.value:
            break
        curr = curr.next
        head_of_second_half = head_of_second_half.next

    # revert the reverse of the second half
    reverse(copied_second)
    if head is None or head_of_second_half is None:
        return True
    return False


def find_mid_point(head: Node):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse(node: Node):
    prev = None
    curr = node
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome 1: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome 2: " + str(is_palindromic_linked_list(head)))


if __name__ == "__main__":
    main()

"""
Time complexity 
The above algorithm will have a time complexity of O(N) where ‘N’ is the number of nodes in the LinkedList.
Space complexity 
The algorithm runs in constant space O(1).
"""
