"""Dictionary related utility functions."""

__author__ = "730613482"

# Define your functions below

from csv import DictReader


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read the rows of the csv file into a list."""
    result: list[dict[str, str]] = []

    file_handle = open(path, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce list of all values in column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], row_num: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first specified rows."""
    result: dict[str, list[str]] = {}
    for col in table:
        result[col] = table[col][0:row_num]
    return result


def select(cols: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce new column based table with specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for selected in names:
        result[selected] = cols[selected]
    return result


def concat(d: dict[str, list[str]], dd: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column based tables."""
    result: dict[str, list[str]] = {}
    for i in d:
        result[i] = d[i]
    for i in dd:
        if i in result:
            result[i] += dd[i]
        else:
            result[i] = dd[i]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Dictionary where every key is a unique value and each value is the count of how many times it appeared."""
    result: dict[str, int] = {}
    for i in values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result