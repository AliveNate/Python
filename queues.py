"""
Remember that a queue is a first in first out method.
First-in-First out

So if you start with Monday, Tuesday, Wednesday
When you pop() it will take off the first one (Monday)

"""
class Queue:

    def __init__(self):
        self.queue = list()

    def addtoq(self, dataval):  # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False

    def removefromq(self):  # Pop method to remove element
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")


TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.removefromq())
print(TheQueue.removefromq())