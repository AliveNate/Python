

class Node:     # Simple node class, with 2 elements. Pass in data param
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:   # A wrapper that contains the nodes
    def __init__(self):
        self.head = Node()

    def insertLast(self, value):
        newNode = Node(value)

    def append(self, data):         # Create the first element of the list
        new_node = Node(data)
        current = self.head
        while current.next != None:  # Cycle through current list until end.
            current = current.next
        current.next = new_node      # Place new node at end of list.

    def length(self):               # Class function to count total number of nodes
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def display(self):          # Display the current contents of list
        elems = []
        current_node = self.head
        while current_node.next != None:        # Until reach the end
            current_node = current_node.next
            elems.append(current_node.data)     # Append nodes to new list for display.
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
        current_idx = 0                     # current index we are looking at
        current_node = self.head            # current node we are looking at
        while True:                         # We already checked if index > length, so this will hit a node, and break
            current_node = current_node.next
            if current_idx == index:        # Cycle until position matches what user sent in
                return current_node.data
            current_idx += 1

    def erase(self, index):                 # index to erase
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        current_idx = 0                     # current index we are looking at
        current_node = self.head            # current node we are looking at
        while True:
            last_node = current_node            # save current as last. erase current, then tie last to new next
            current_node = current_node.next    # last_node     --> xxx -->     current_node.next
            if current_idx == index:            # if at index that user provided to delete
                last_node.next = current_node.next  # dont have to delete, just change pointer to new/next node
                return
            current_idx += 1




# ----------------------------------------------------------
my_list = LinkedList()
my_list.display()       # Empty list = empty brackets   []
my_list.append(1)
my_list.append(2)
my_list.display()       # [1, 2]
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
print(f'Element at 2nd Index:  {my_list.get(2)}')
print("Delete the element at the 3rd index")
my_list.erase(3)
my_list.display()

