"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730613482"


class Simpy:
    """Simpy object to handle lists."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Initialize simpy object."""
        self.values = values

    def __repr__(self) -> str:
        """Create a string representation of simpy object."""
        return f"Simpy({self.values})"

    def fill(self, value: float, num: int) -> None:
        """Fill values with given number of floats."""
        self.values = []
        for _ in range(num):
            self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill values with range of values."""
        self.values = []
        for i in range(int(start // step), int(stop // step)):
            self.values.append(i * step)
        
    def sum(self) -> float:
        """Sum of all values in values."""
        return sum(self.values)

    def __add__(self, other: Union[Simpy, float]) -> Simpy:
        """Handle addition of Simpy objects and floats."""
        if isinstance(other, self.__class__):
            assert len(self.values) == len(other.values)
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] + other.values[i])
            ret = Simpy(result)
            return ret
        else:
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] + other)
            ret = Simpy(result)
            return ret

    def __pow__(self, other: Union[Simpy, float]) -> Simpy:
        """Handle power of Simpy objects and floats."""
        if isinstance(other, self.__class__):
            assert len(self.values) == len(other.values)
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] ** other.values[i])
            ret = Simpy(result)
            return ret
        else:
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] ** other)
            ret = Simpy(result)
            return ret

    def __eq__(self, other: Union[Simpy, float]) -> list[bool]:
        """Handle equality of Simpy objects and floats."""
        if isinstance(other, self.__class__):
            assert len(self.values) == len(other.values)
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] == other.values[i])
            ret = Simpy(result)
            return ret
        else:
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] == other)
            ret = Simpy(result)
            return ret

    def __gt__(self, other: Union[Simpy, float]) -> list[bool]:
        """Handle greater than of Simpy objects and floats."""
        if isinstance(other, self.__class__):
            assert len(self.values) == len(other.values)
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] > other.values[i])
            ret = Simpy(result)
            return ret
        else:
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] > other)
            ret = Simpy(result)
            return ret

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Get item from the list."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
            for i in range(len(rhs.values)):
                if rhs.values[i]:
                    result.append(self.values[i])
            return Simpy(result)
    
