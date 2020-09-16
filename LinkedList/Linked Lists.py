from __future__ import annotations

# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, item, Node : next = None):
        self.item = item  # Assign data
        self.next = None  # Initialize
        # next as null



# Linked List class contains a Node object
class LinkedList:

    # Function to initialize instance variables
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.size = 0
        if len(args) == 1:
            try:
                # try to insert each item
                for x in args[0]:
                    self.append(x)
            except TypeError:
                # exception raised if item not iterable so just insert it
                self.append(args[0])
        else:
            # 0 or 2 or more arguments so iterate over them and insert them
            for x in args:
                self.append(x)

    #-------------------------------------------------------------------------------------------------------------------

    def append(self, item):
        """
        adds item at the end
        @param: item to add
        @return: NONE
       """
        newNode = Node(item)

        if self.head is None or self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    #-------------------------------------------------------------------------------------------------------------------

    def __len__(self):
        return self.size

    #-------------------------------------------------------------------------------------------------------------------

    def getItemAtHead(self):
        if self.head is None:
            raise IndexError("Item called on an empty List")
        else:
            return self.head.item

    #-------------------------------------------------------------------------------------------------------------------

    def getItemAtTail(self):
        if self.tail is None:
            raise IndexError("Item called on an empty List")
        else:
            return self.tail.item

    #-------------------------------------------------------------------------------------------------------------------

    def appendAtHead(self, item):
        """
        adds item at head
        @param: item to add
        @return: NONE
        """
        newNode = Node(item)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    #-------------------------------------------------------------------------------------------------------------------

    def pop(self):
        """
        WHAT
        remove and return last item from the list
        @param: NONE
        @return: item at the end
        """
        item = self.tail.item

        if self.head is None:
            raise IndexError("Pop called on an empty list")
        else:
            self.size -= 1
            curNode = self.head
            for i in range(self.size - 1):
                curNode = curNode.next

            curNode.next = None
            self.tail = curNode
        return item

    #-------------------------------------------------------------------------------------------------------------------

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.item
            node = node.next

    #-------------------------------------------------------------------------------------------------------------------

    def __sub__(self, other):
        l1 = LinkedList()

        node1 = self.head
        otherNode = other.head

        # Main code, what we are computing: l3 = l1 - l2
        # Other is l2, self is l1
        if len(other) >= len(self):
            for i in range(len(self)):
                l1.append(node1.item - otherNode.item)
                node1 = node1.next
                otherNode = otherNode.next

        return l1


def main():

    def testAppend():
        pass
    def testAppendAtHead():
        pass
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    temp = []

    for i in range(5):
        l1.append(i)

    for i in l1:
        temp.append(i)
    print("L1:", temp)
    temp.clear()

    for i in range(5,0,-1):
        l2.append(i)
    for i in l2:
        temp.append(i)
    print("L2:", temp)
    temp.clear()

    l3 = l1 - l2
    for i in l3:
        temp.append(i)
    print("L3:", temp)
    temp.clear()
    

    x = 5
main()