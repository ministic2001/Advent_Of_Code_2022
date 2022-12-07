import sys
import os
sys.path.insert(0, r"./file_reader")    #import file_reader function from file_reader/file_reader.py

from file_reader import file_reader

FILE: str = r"raw data.txt"
CURRENT_WORKING_DIRECTORY: str = os.path.dirname(os.path.abspath(__file__))

def data_to_elve_calories(raw_data: str) -> list[list[int]]:
    """
    Converts the raw data into a 2D array of calories, where each row represents the individual calories an elf is carrying.

    raw_data: The raw data from advent of code day 1.

    return: 2D list array, where each row of array represents the individual calories an elf is carrying.
    """
    spaced_data = raw_data.replace("\n", " ")   # 1 space = same elf, next calorie. 2 space = next elf
    each_elf_array = spaced_data.split("  ")    # Convert to ['1234 4321 3943', '5834 29134'] based on double spaces
    
    for elf_number, elf_calories in enumerate(each_elf_array):
        each_elf_array[elf_number] = list(map(int, elf_calories.split(" ")))
    return each_elf_array

def array_summer_2d(array_int_2D: list[list[int]]) -> list[int]:
    """
    Sums each element in a 2D array.

    array_int_2D: The 2D array input of integers.

    return: List of int array, this case, total number of calories each elf is carrying.
    """
    for array_number, int_array in enumerate(array_int_2D):
        array_int_2D[array_number] = sum(int_array)
    return array_int_2D

def get_top_3_highest_elves(each_elf_total_calories_array: list[int]) ->list[list[int]]:
    """
    Get the top 3 highest calorie-carrying elves.

    each_elf_total_calories_array: Number of calories each elf is carrying

    return: A 2D array where each row is in the format of [elf number, number of calories]
    """
    TOP_NO: int = 3
    top_no_calories_array: list[list[int]] = []
    
    for _ in range(TOP_NO):
        most_calories: int = max(each_elf_total_calories_array)
        most_calories_elf: int = each_elf_total_calories_array.index(most_calories)
        top_no_calories_array.append([most_calories_elf, most_calories])
        each_elf_total_calories_array.pop(most_calories_elf)
    return top_no_calories_array




def main():
    raw_data: str = file_reader(CURRENT_WORKING_DIRECTORY + r"/" + FILE)

    each_elf_array: list[list[int]] = data_to_elve_calories(raw_data)
    each_elf_total_calories_array: list[int] = array_summer_2d(each_elf_array)
    top_3_elves_calories: list[list[int]] = get_top_3_highest_elves(each_elf_total_calories_array)
    top_3_elves: list[int] = [top_3_elves[0] for top_3_elves in top_3_elves_calories]
    top_3_calories: list[int] = [top_3_calories[1] for top_3_calories in top_3_elves_calories]

    print(f"The top 3 calories carried by 3 elves is {', '.join(map(str, top_3_calories))} by elves no {', '.join(map(str, top_3_elves))} respectively, totalling to {sum(top_3_calories)} calories!")

if __name__ == "__main__":
    main()