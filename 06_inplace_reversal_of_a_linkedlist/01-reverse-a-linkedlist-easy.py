"""
Problem Statement
Given the head of a Singly LinkedList, reverse the LinkedList.
 Write a function to return the new head of the reversed LinkedList.
"""
from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head: Node):
    if not head:
        return None
    prev = None

    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


if __name__ == "__main__":
    main()

"""
Time complexity 
The time complexity of our algorithm will be O(N) where ‘N’ is the total number 
of nodes in the LinkedList.

Space complexity 
We only used constant space, therefore, the space complexity of our algorithm is
 O(1).
"""
