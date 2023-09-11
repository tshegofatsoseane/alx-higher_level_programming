#!/usr/bin/python3
"""Define classes for linked list."""


class Node:
    """Represent node in linked list."""

    def __init__(self, data, next_node=None):
        """Initialize new Node.

        Args:
            data (int): New node data.
            next_node (Node): Next node of new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get and set data of new node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get and set next node of the newNode."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent linked list."""

    def __init__(self):
        """Initalize linked List."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new Node to linked list.

        Args:
            value (Node): Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the representation of a linked list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

