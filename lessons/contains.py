"""Example implementing a list """

# function name: contains
# we will have 2 parameters: needle (str), haystack (list[str])
# return true if needle is found in haystack at least once and false otherwise

def contains(needle: str, haystack: list) -> bool:
    i: int = 0
    while(i<len(haystack)):
        if(needle==haystack[i]):
            return True
        i+=1
    return False


needle:str="d"
haystack: list = list()
haystack = ["a","b","c"]
print(contains(needle, haystack))