from __future__ import annotations

class ListNode:
    def __init__(self, value, next: ListNode = None):
        self.value = value
        self.next = next

class LinkedList:
    # Method: function inside a class

    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.size = 0

        # if only one argument, see if i can iterate over it
        if len(args) == 1:
            try:
                # try to append each item
                for i in args[0]:
                    self.append(i)
            except TypeError:
                # exception if not iterable, just append that item
                self.append(args[0])
        else:
            # if 0 or 2 or more items, iterate over them and append the items
            for i in args:
                self.append(i)

    def append(self, item):
        # if the list is empty
        if self.size == 0 or self.head == None:
            # make a node with item
            node = ListNode(item)
            # set head and tail to the node
            self.head = node
            self.tail = node
        # else if the list is not empty
        else:
            # make a node with item
            node = ListNode(item)
            # the current tail will point to the new node
            self.tail.next = node
            # make the tail the new node we just added
            self.tail = node
        # increase size
        self.size += 1

    def __len__(self):
        return self.size

    def __add__(self, other):
        """
        add two LinkedLists together
        @param 
        @return
        """
        l3 = LinkedList()
        node = self.head
        for i in range(len(self)):
            l3.append(node.value)
            node = node.next

        node = other.head
        for i in range(len(other)):
            l3.append(node.value)
            node = node.next

        return l3

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def __sub__(self, other):
        l3 = LinkedList()

        if len(self) < len(other):
            raise Exception("Cannot subtract from list less than second list")
        else:
            for i in self:
                if i not in other:
                    l3.append(i)

        return l3

def main():

    # l1 = LinkedList(1, 2, 3, 4)
    l1 = LinkedList(1, 2, 3, 4)

    for i in l1:
        print(i, end=" ")


main()