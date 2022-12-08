import sys
import os
sys.path.insert(0, r"./file_reader")    #import file_reader function from file_reader/file_reader.py

from file_reader import file_reader
from enum import Enum

FILE: str = r"raw data.txt"
CURRENT_WORKING_DIRECTORY: str = os.path.dirname(os.path.abspath(__file__))

class RockPaperScissors(Enum):

    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"
    
    
    def single_round_score(encrypted_row: list[str, str]) -> int:
        """
        Converts the encrypted/secret row to a score based on the scoring system by the new elves Rock Paper Scissors version

        encrypted_row: One game where left of list is what the opponent chooses and right of list is what I chose

        return: Score based off the scoring system of the new elves Rock Paper Scissors
        """
        score:int = 0

        opponent_chooses: Enum = RockPaperScissors(encrypted_row[0])
        lose_draw_win: Enum = RockPaperScissors(encrypted_row[1])

        match lose_draw_win:
            case RockPaperScissors.DRAW:
                score += 3
                myself_chooses: Enum = opponent_chooses
            case RockPaperScissors.WIN:
                score += 6
                match opponent_chooses:
                    case RockPaperScissors.ROCK:
                        myself_chooses: Enum = RockPaperScissors.PAPER
                    case RockPaperScissors.PAPER:
                        myself_chooses: Enum = RockPaperScissors.SCISSORS
                    case RockPaperScissors.SCISSORS:
                        myself_chooses: Enum = RockPaperScissors.ROCK
            case RockPaperScissors.LOSE:
                match opponent_chooses:
                    case RockPaperScissors.ROCK:
                        myself_chooses: Enum = RockPaperScissors.SCISSORS
                    case RockPaperScissors.PAPER:
                        myself_chooses: Enum = RockPaperScissors.ROCK
                    case RockPaperScissors.SCISSORS:
                        myself_chooses: Enum = RockPaperScissors.PAPER
        
        match myself_chooses:
            case RockPaperScissors.ROCK:
                score += 1
            case RockPaperScissors.PAPER:
                score += 2
            case RockPaperScissors.SCISSORS:
                score += 3

        
        return score

def data_to_2D_array(encrypted_strategy_guide_raw: str) -> list[list[str]]:
    """
    Converts the raw data into a 2D array where an elment in the array represents an encrypted game

    encrypted_strategy_guide_raw: The raw data given by some elf

    return: A 2D array containing an encrypted game as the element.
    """
    encrypted_strategy_guide = encrypted_strategy_guide_raw.split("\n")
    encrypted_strategy_guide = [encrypted_game.split(" ") for encrypted_game in encrypted_strategy_guide]
    
    return encrypted_strategy_guide

def main():
    encrypted_strategy_guide_raw: str = file_reader(CURRENT_WORKING_DIRECTORY + r"/" + FILE)
    encrypted_strategy_guide = data_to_2D_array(encrypted_strategy_guide_raw)

    score: int = 0
    for encrypted_row in encrypted_strategy_guide:
        score += RockPaperScissors.single_round_score(encrypted_row)
    
    print(f"By following this new encrypted guide, you would score {score} points")

if __name__ == "__main__":
    main()