"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last

__author__ = "Your PID"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3

def test_last() -> None:
    """Test last function."""


def test_value_at() -> None:
    """Test value at function."""


def test_max() -> None:
    """Test max function."""


def test_max() -> None:
    """Test max function."""


def test_linkify() -> None:
    """Test linkify function."""

def test_scale() -> None:
    """Test scale function."""


