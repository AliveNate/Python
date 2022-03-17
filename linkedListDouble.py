"""
Following is the features of doubly linked list.

    Doubly Linked List contains a link element called first and last.
    Each link carries a data field(s) and two link fields called next and prev.
    Each link is linked with its next link using its next link.
    Each link is linked with its previous link using its previous link.
    The last link carries a link as null to mark the end of the list.

We create a Doubly Linked list by using the Node class.
Now we use the same approach as used in the Singly Linked Lis,
    but the head and next pointers will be used for proper assignation
    to create two links in each of the nodes in addition to the data present in the node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None

    def push(self, newVal):  # Adding data elements
        newNode = Node(newVal)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def insert(self, prev_node, newVal):  # Define the insert method to insert the element
        if prev_node is None:
            return
        newNode = Node(newVal)
        newNode.next = prev_node.next
        prev_node.next = newNode
        newNode.prev = prev_node
        if newNode.next is not None:
            newNode.next.prev = newNode

    def append(self, newVal):  # Define the append method to add elements at the end
        newNode = Node(newVal)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = newNode
        newNode.prev = last
        return

    def listprint(self, node):  # Print the Doubly Linked list
        while (node is not None):
            print(node.data),
            last = node
            node = node.next


dllist = doubly_linked_list()
dllist.push(12)
dllist.append(9)    # Appending to a doubly linked list will add the element at the end.
dllist.push(8)
dllist.push(62)
dllist.append(45)   # Appending to a doubly linked list will add the element at the end.
dllist.insert(dllist.head.next, 13)  # inserts the new node at the third position from the head
dllist.listprint(dllist.head)