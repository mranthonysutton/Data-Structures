from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # check if empty -> if empty put node at root
        # If not empty, compare if new < node.value
        if self.value:
            # go left (leftnode.insert)
            if value < self.value:

                # If self.left is valid insert, if not
                # create that value and return it
                if self.left:
                    self.left.insert(value)
                    return
                else:
                    self.left = BinarySearchTree(value)
                    return

            # if new > node.value, go right (rightnode.insert value)
            else:
                # if self.right is valid insert, if not
                # Create that value and return it
                if self.right:
                    self.right.insert(value)
                    return
                else:
                    self.right = BinarySearchTree(value)
                    return
        else:
            self.value = value

    def contains(self, target):
        """
        If node.value == findvalue
            return True
        else
            if find < node.value
                if node left
                    find on left node
                else
                    find on right node
        """
        if self.value:
            if target == self.value:
                return True
            elif target <= self.value and self.left:
                return self.left.contains(target)
            elif target >= self.value and self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        """
        If node to the right
            Grab the right node
        else:
            return node.value
        """
        if not self.right:
            return self.value

        elif self.value <= self.right.value:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # the callback function will pass in the self.value
        cb(self.value)

        # if right, call the cb on the right node, else, call on the left node
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
