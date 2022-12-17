__author__ = "730613482"

"""Dictionary python script."""

def invert(dictionary: dict([str, str])) -> dict([str,  str]):
    new_dict: dict(str, str) = {}
    for key, value in dictionary:
        duplicate: bool = False
        for k, v in dictionary:
            if value == v:
                duplicate = True
            if duplicate:
                raise KeyError("error message of your choice here!")
        new_dict.append(value, key)
    return new_dict
       

def favorite_color(names_colors: dict([str, str])) -> str:
    high: int = 0
    word: str = ""
    assert len(names_colors) > 0
    for k, v in names_colors:
        count: int = 0
        for kk, vv in names_colors:
            if v == vv:
                count += 1
        if count > high:
            high = count
            word = v
    return word
        


def count(int) -> int:
    pass

favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) 