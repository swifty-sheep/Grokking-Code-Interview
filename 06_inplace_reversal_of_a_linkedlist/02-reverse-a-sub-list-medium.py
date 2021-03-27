"""
Problem Statement
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the
LinkedList from position ‘p’ to ‘q’.
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


def reverse_sub_list_my_sol(head, p, q):
    position = 1
    current = head
    before_p = None
    while current and position < p:
        before_p = current
        current = current.next
        position += 1
    prev = None
    start_p = current
    while current and position <= q:
        next = current.next
        current.next = prev
        prev = current
        current = next

        position += 1

    # link the sub-list back to the main list
    before_p.next = prev
    start_p.next = current

    return head


def reverse_sub_list(head, p, q):
    if p == q:
        return head
    # after skipping p-1 nodes, current will point to pth node
    current, previous = head, None
    i = 0
    while current is not None and i < p-1:
        previous = current
        current = current.next
        i += 1

    # interested in 3 parts of the linkedlist, 1. before index p,
    # 2. between p and q, 3. after index q
    last_node_of_first_part = previous
    last_node_of_sub_list = current
    next = None

    i = 0
    # reverse nodes between p and q
    print(previous.value, current.value)
    while current is not None and i < q-p+1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    # connect with the first part
    if last_node_of_first_part:
        last_node_of_first_part.next = previous
    else:
        head = previous
    # connect with the last part
    last_node_of_sub_list.next = current
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_sub_list_my_sol(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()
    print("\n")
    head_one = Node(1)
    head_one.next = Node(2)
    head_one.next.next = Node(3)
    head_one.next.next.next = Node(4)
    head_one.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end="")
    head_one.print_list()
    result = reverse_sub_list_my_sol(head_one, 2, 4)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


if __name__ == "__main__":
    main()

"""
Time complexity 
The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.
Space complexity 
We only used constant space, therefore, the space complexity of our algorithm is O(1).
"""

"""
Solution 
The problem follows the In-place Reversal of a LinkedList pattern. 
We can use a similar approach as discussed in Reverse a LinkedList. Here are the steps we need to follow:
1. Skip the first p-1 nodes, to reach the node at position p.
2. Remember the node at position p-1 to be used later to connect with the reversed sub-list.
3. Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
4. Connect the p-1 and q+1 nodes to the reversed sub-list.
"""