import sys
import os
sys.path.insert(0, r"./file_reader")    #import file_reader function from file_reader/file_reader.py

from file_reader import file_reader

FILE: str = r"raw data.txt"
CURRENT_WORKING_DIRECTORY: str = os.path.dirname(os.path.abspath(__file__))

def rucksack_group_checker(rucksack_group: list[str, str, str]) -> str:
    """
    Checks if within a group of 3 rucksack there is any common characters

    rucksack_group: An array of 3 rucksack

    return: The common item/character between the 3 rucksacks
    """
    for character_to_compare in set(rucksack_group[0]):
        if (character_to_compare in rucksack_group[1]) and (character_to_compare in rucksack_group[2]):
            return character_to_compare

def character_to_priority(character: str) -> int:
    """
    Converts character into priority value based on the following rules:
        - Lowercase item types a through z have priorities 1 through 26.
        - Uppercase item types A through Z have priorities 27 through 52.
    
    character: Single character as input

    return: priority value
    """
    ascii_value: int = ord(character)

    if character >= "a": # Lower case only
        priority_value: int = (ascii_value + 7) % 26 + 1
    else: # Upper case only
        priority_value: int = (ascii_value + 13) % 26 + 27

    return priority_value

def single_rucksack_group_priority(rucksack_single_group: list[str, str, str]) -> int:
    """
    Converts one rucksack group into priority value.

    rucksack_single_group: 3 rucksack (strings) in an array.

    return: priority_value
    """

    common_character: str = rucksack_group_checker(rucksack_single_group)
    priority_value: int = character_to_priority(common_character)

    return priority_value

def rucksack_grouping(rucksack_raw: str) -> list[list[str, str, str]]:
    """
    Convert the rucksack raw data into an array of groups of 3 rucksack.

    rucksack_raw: The rucksack raw data provided by Advent Of Code 2022.

    return: An array of rucksack which are groups of 3.
    """
    GROUPING: int = 3

    rucksack_array: list[str] = rucksack_raw.split("\n")
    rucksack_group_count: int = len(rucksack_array)//GROUPING
    rucksack_group_array: list[list[str, str, str]] = [rucksack_array[rucksack_group_number * GROUPING:rucksack_group_number * GROUPING + GROUPING] for rucksack_group_number in range(rucksack_group_count)]

    return rucksack_group_array

def main():
    rucksack_raw: str = file_reader(CURRENT_WORKING_DIRECTORY + r"/" + FILE)
    rucksack_group_array: list[list[str, str, str]] = rucksack_grouping(rucksack_raw)

    priority_total: int = 0
    for rucksack_single_group in rucksack_group_array:
        priority_total += single_rucksack_group_priority(rucksack_single_group)
    
    print(f"Total sum of priorities is {priority_total}.")

if __name__ == "__main__":
    main()