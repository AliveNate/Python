

class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):  # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self):     # Use peek to look at the top of the stack
        return self.stack[-1]

    def remove(self):   # Use list pop method to remove element
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return(f'Removed: {self.stack.pop()}')

AStack = Stack()
#
AStack.add("Mon")
AStack.add("Tue")
print(AStack.peek())
#
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())
#
print(AStack.remove())
print(AStack.remove())
