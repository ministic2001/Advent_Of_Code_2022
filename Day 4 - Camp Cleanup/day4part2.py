import sys
import os
sys.path.insert(0, r"./file_reader")    #import file_reader function from file_reader/file_reader.py

from file_reader import file_reader

FILE: str = r"raw data.txt"
CURRENT_WORKING_DIRECTORY: str = os.path.dirname(os.path.abspath(__file__))

def convert_to_range_pair_array(raw_data: str) -> list[list[list[int, int], list[int, int]]]:
    """
    Converts the raw data into a range array. For example, given\n
    13-53,17-82\n
    32-32,32-42\n

    This will be converted to [[[13, 53], [17, 82]], [[32, 32], [32, 42]]]

    raw_data: The raw data from Advent Of Code 2022

    return: A range array, example structure shown above
    """
    range_row_array: list[str] = raw_data.split("\n")
    range_pair_array_unformatted: list[list[str, str]] = [range_row.split(",") for range_row in range_row_array]
    range_pair_array_formatted: list[list[list[int, int], list[int, int]]] = [[list(map(int, range_row[0].split("-"))), list(map(int, range_row[1].split("-")))] for range_row in range_pair_array_unformatted]

    return range_pair_array_formatted

def check_if_overlap(range_pair: list[list[int, int], list[int, int]]) -> bool:
    """
    Check if any pair range overlaps

    range_pair: The pair of ranges to check

    return: True or False
    """
    pair_range_first: list[str, str] = range_pair[0]
    pair_range_second: list[str, str] = range_pair[1]

    return (pair_range_first[1] >= pair_range_second[0] or pair_range_first[1] >= pair_range_second[1]) and (pair_range_second[1] >= pair_range_first[0] or pair_range_second[1] >= pair_range_first[1])
    return (True in [pair_range_first[1] >= pair_range_second_value for pair_range_second_value in pair_range_second]) and (True in [pair_range_second[1] >= pair_range_first_value for pair_range_first_value in pair_range_first]) # Another cool alternative
        
def main():
    raw_data: str = file_reader(CURRENT_WORKING_DIRECTORY + r"/" + FILE)
    range_pair_array: list[list[list[int, int], list[int, int]]] = convert_to_range_pair_array(raw_data)

    pair_count: int = 0
    for range_pair in range_pair_array:
        if check_if_overlap(range_pair):
            pair_count += 1
    
    print(f"There are {pair_count} assignment pairs where the ranges have at least a value that overlaps")

if __name__ == "__main__":
    main()