import sys
import os
sys.path.insert(0, r"./file_reader")    #import file_reader function from file_reader/file_reader.py

from file_reader import file_reader

FILE: str = r"raw data.txt"
CURRENT_WORKING_DIRECTORY: str = os.path.dirname(os.path.abspath(__file__))

def compartment_checker(compartment_1: str, compartment_2: str) -> str:
    """
    Checks first compartment and second compartment of a racksack and see if there is any common characters

    compartment_1: First compartment in a rucksack
    compartment_2: Second compartment in a rucksack

    return: The common item/character between 2 compartments
    """
    for character_to_compare in set(compartment_1):
        if character_to_compare in compartment_2:
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

def single_rucksack_priority(one_rucksack: str) -> int:
    """
    Converts one rucksack into priority value

    one_rucksack: self-explanatory

    return: priority_value
    """
    rucksack_length = len(one_rucksack)
    compartment_1:str = one_rucksack[:rucksack_length//2]
    compartment_2:str = one_rucksack[rucksack_length//2:]
    common_character: str = compartment_checker(compartment_1, compartment_2)
    priority_value: int = character_to_priority(common_character)

    return priority_value

def main():
    rucksack_raw: str = file_reader(CURRENT_WORKING_DIRECTORY + r"/" + FILE)
    rucksack: list[str] = rucksack_raw.split("\n")
    single_rucksack_priority(rucksack[0])

    priority_total: int = 0
    for one_rucksack in rucksack:
        priority_total += single_rucksack_priority(one_rucksack)
    
    print(f"Total sum of priorities is {priority_total}.")

if __name__ == "__main__":
    main()