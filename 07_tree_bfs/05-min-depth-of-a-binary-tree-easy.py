"""
Problem Statement

Find the minimum depth of a binary tree.
The minimum depth is the number of nodes along the shortest path from the root
node to the nearest leaf node.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    result = 0
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    level = 1
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left is None and node.right is None:
                return level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return level


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


if __name__ == "__main__":
    main()

"""
Time complexity 
The time complexity of the above algorithm is O(N), where ‘N’ is the total 
number of nodes in the tree. 

This is due to the fact that we traverse each node once.
Space complexity 
The space complexity of the above algorithm will be O(N)O which is required for 
the queue. 
Since we can have a maximum of N/2 nodes at any level (this could happen only at
the lowest level), therefore we will need O(N) space to store them in the 
queue.
"""

"""
Similar Problems 
Problem 1: Given a binary tree, find its maximum depth (or height).
Solution: We will follow a similar approach. Instead of returning as soon as we 
find a leaf node, we will keep traversing for all the levels, incrementing 
maximumDepth each time we complete a level. 
Here is what the code will look like:
"""


def find_maximum_depth(root):
    result = 0
    if root is None:
        return result
    queue = deque()
    queue.append(root)

    level = 0
    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return level


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))


if __name__ == "__main__":
    main()
