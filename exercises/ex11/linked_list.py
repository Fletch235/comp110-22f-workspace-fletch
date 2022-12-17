"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "Your PID"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next == None:
            return head.data
        else:
            return last(head)


def value_at(head: Optional[Node], index: int) -> int:
    """Return the value at a given index."""
    if head is None:
        raise ValueError("value at cannot be called with None")
    else:
        if index == 0:
            return head.data
        else:
            return value_at(head.next, index - 1)
    

def max(head: Optional[Node], values: Optional[list[int]] = []) -> int:
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        if head.next == None:
            best: int = values[0]
            for value in values:
                if value > best:
                    best = value
            return best
        else:
            values.append(head.data)
            return max(head.next, values)
        

def linkify(items: list[int]) -> Optional[Node]:
    if len(items) == 0:
        return None
    else:  
        i: int = len(items)
        prev: Node = Node(items[i - 1], None)
        i -= 1
        while i > 0:
            next: Node = Node(items[i - 1], prev)
            prev = next
            i -= 1
        return prev


def scale(head: Optional[Node], factor: int, values: Optional[list[int]] = []) -> Optional[Node]:
    if head is None:
        raise ValueError("Cannot call scale with None")    
    else:
        if head.next == None:
            values.append(head.data)
            for i in range(len(values)):
                values[i] *= factor
            return linkify(values)
        else:
            values.append(head.data)
            return scale(head.next, factor, values)

