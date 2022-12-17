__author__ = "730613482"


def all(list_of_ints: list, int_check: int) -> bool:
    i:int = 0
    while(i<len(list_of_ints)):
        if(int_check != list_of_ints[i]):
            return False
        i+=1
    return True


def max(list_of_ints: list) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    large:int = -1000000000000
    i:int = 0
    while(i<len(list_of_ints)):
        if(large < list_of_ints[i]):
            large = list_of_ints[i]
        i+=1
    return large


def is_equal(list_one: list, list_two: list)