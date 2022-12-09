import sys
import os
sys.path.insert(0, r"./file_reader")    #import file_reader function from file_reader/file_reader.py

from file_reader import file_reader
# from typing import Self -> Whoops turns out its a 3.11 support only

FILE: str = r"raw data.txt"
CURRENT_WORKING_DIRECTORY: str = os.path.dirname(os.path.abspath(__file__))

class CrateStack:
    def __init__(self, original_crates: list[str]) -> None:
        """
        Initialize the Crate Stack

        original_crates: The crates which were originally in the crate stack
        """
        self.crates = original_crates
    
    def get_top_crate(self) -> str:
        """
        Obtain the crate value at the top of crate stack

        return: Value of crate
        """
        if len(self.crates) > 0:
            return self.crates[-1]
        else:
            return "Crate is empty!"

    def push(self, crates_received: list[str]) -> None:
        """
        Add at least a crate at the top of the crate stack
        
        crates: The crate to be added on the top of stack
        """
        self.crates += crates_received

    def pop(self, crate_removal_number: int) -> list[str]:
        """
        Remove at least a crate at the top of crate stack

        crate_removal_number: Number of crates to be removed from top of crate stack

        return: A list of crates that is removed from top of crate stack
        """
        if len(self.crates) > 0:
            crates_removed: list[str] = self.crates[-crate_removal_number:]
            self.crates = self.crates[:-crate_removal_number]
            return crates_removed

    def move_crates(self, other_crate_stack, move_count: int) -> None: # Class Type hinting only at 3.11
        """
        Move the crate x numver of times from one crate to another crate.

        self: The crate stack to be moved
        other_crate_stack: The crate stack to receive
        move_count: The number of times the crate is moved
        """
        other_crate_stack.push(self.pop(move_count))
    
    def __repr__(self) -> list[str]:
        """
        Return a list of crates of a crate stack if the class is called

        return: A list of crates
        """
        return repr(self.crates)

def crate_instructions_split(raw_schemata: str) -> tuple[list[list[int, int, int]], list[list[str]]]:
    """
    Converts the raw data into a bunch of list

    raw_schemata: The raw data obtained from Advent Of Code 2022 input
    """

    def instruction_list_siever(instruction_list) -> list[list[int, int, int]]: # Did I just create an entire function just for a 1-liner code...!? I thought it was a lot harder. Welp, too much effort is wasted if I erase this function :P
        """
        Sieve just the numbers from the worded instruction. Python read code, not english!\n
        Example - move 11 from 7 to 9 -> [11, 7, 9]

        instruction_list: A list of worded instructions

        return: A list of 3 integer instructions that is in the format of [move count, from crate, to crate]
        """
        instruction_list_clean: list[list[int, int, int]] = [list(map(int, instruction.split(" ")[1:6:2])) for instruction in instruction_list]

        return instruction_list_clean
    
    def crate_stack_ordered_list(crates_unordered: list[str]) -> list[list[str]]:
        """
        Conerts the ascii art of crates into the crate stack order, with each crate stack containing a list of crates they have.

        crates_unordered: ASCII crate art obtained from Advent Of Code

        return: A list of crate stack, where each crate stack contains a list of crates from bottom to top
        """
        crates_ordered_by_stack: list[list[str]] = [[] for _ in range(9)]

        crates_unordered: list[list[str]] = [crate_line.replace("[", "").replace("]", "").split(" ") for crate_line in crates_unordered]
        crates_ordered_by_level: list[list[str]] = [" ".join(crate_line).replace("    ", " ").split(" ") for crate_line in crates_unordered]

        # This will end up with an upside down crate order where the top crate appears first and bottom crate appears last in the crate stack
        for crate_height_contents in crates_ordered_by_level:
            for stack_number, crate in enumerate(crate_height_contents):
                if crate != "":
                    crates_ordered_by_stack[stack_number].append(crate)

        crates_ordered_by_stack = [crate_stack_upsidedown[::-1] for crate_stack_upsidedown in crates_ordered_by_stack]
        
        return crates_ordered_by_stack
        
    
    raw_schemata: list[str] = raw_schemata.split("\n")

    crates_unordered: list[str] = raw_schemata[:8]
    instruction_list: list[str] = raw_schemata[10:]

    instruction_list_clean: list[list[int, int, int]] = instruction_list_siever(instruction_list)
    crates_ordered: list[list[str]] = crate_stack_ordered_list(crates_unordered)

    return instruction_list_clean, crates_ordered

def instructions_compute(crate_stack_array: list[CrateStack], instruction_list: list[list[int, int, int]]) -> list[CrateStack]:
    """
    Compute a list of instructions to the crate stack

    crate_stack_array: An array of crate stack
    instruction_list: a list of instructions

    return: A list of crate stack computed after following a list of instructions
    """
    for instruction in instruction_list:
        crate_stack_array[instruction[1] - 1].move_crates(crate_stack_array[instruction[2] - 1], instruction[0])
    
    return crate_stack_array

def main():
    raw_schemata: str = file_reader(CURRENT_WORKING_DIRECTORY + r"/" + FILE)
    crate_instructions_split(raw_schemata)
    
    instruction_list_clean: list[list[int, int, int]]
    crates_ordered: list[list[str]]
    instruction_list_clean, crates_ordered = crate_instructions_split(raw_schemata)

    crate_stack_array: list[CrateStack] = [CrateStack(crate_stack_contents) for crate_stack_contents in crates_ordered]
    crate_stack_array = instructions_compute(crate_stack_array, instruction_list_clean)

    top_of_each_crate_stack = [crate_stack.get_top_crate() for crate_stack in crate_stack_array]
    
    print(f"The top of each crate stack is {''.join(top_of_each_crate_stack)}.")

if __name__ == "__main__":
    main()