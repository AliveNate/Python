"""Binary tree
             2
            / \
           1   5
               /\
              4  6
                  \
                   7
"""
class Node:

    def __init__(self, data):

        self.left = None        # Node has left/right. These are empty if nothing less/greater
        self.right = None
        self.data = data

    def insert(self, data):     # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)  # If new data is LESS, and left child is empty. Insert
                else:
                    self.left.insert(data)  # Check left child, to compare new vs left child.
            elif data > self.data:          # Check or greater than comparisons, insertions.
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):  # findval method to compare the value with nodes
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.findval(lkpval)
        else:
            return '\n' + str(self.data) + ' is found'

    def PrintTree(self):    # Print the tree. Lowest value nodes first.
        if self.left:       # If self.left exists, i.e. is not NONE
            self.left.PrintTree()  # Check is we can go any further left (LESS) on current Node
        print(self.data)    # If Nothing to the left of a specific node, then print data
        if self.right:      # Move to right node, check if it has left/right children.
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
#
root.insert(4)
root.insert(6)
root.insert(7)
root.insert(1)
root.insert(2)
root.insert(5)
root.insert(13)

root.PrintTree()

print(root.findval(7))
print(root.findval(14))

