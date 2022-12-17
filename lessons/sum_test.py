"""tests for sum function"""


from lessons.sum import sum


def test_sum_empty() -> None:
    xs: list = []
    assert sum(xs) == 0.0

def test_sum_single() -> None:
    xs: list = [110.0]
    assert sum([110.0])