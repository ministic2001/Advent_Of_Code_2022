# Advent of Code 2022, coded by ministic2001

## Introduction
Advent of Code is a yearly christmas coding event that challenges on various coding logic. 
This year, I decided to try coding since I am bored and on holiday on December. I also want to try various **Python** coding styles and practices, especially with the ```if __name__ == "__main__":```  

### New Python Styles
The folowing list are style changes that I am attempting to fit better to the standard coding practices:
1. Main function eg. ```if __name__ == "__main__":``` 
2. Function reuse placed in a new file (Like `file_reader()`)
3. Type hinting in variables/constants and functions eg
    - `TOP_NO: int = 3`
    - `def file_reader(full_directory_filename: str) -> str:`
4. Better function naming, aka self descriptive function names
5. Function commenting, as based on [this blog](https://blog.openreplay.com/the-art-of-writing-good-code-comments/) and [this stackoverflow answer](https://stackoverflow.com/questions/2357230/what-is-the-proper-way-to-comment-functions-in-python) by Shwetabh Shekhar

## File Directory Structure
### Reasoning
As preperation for CTF Writeups, I want to have a proper file directory structure inside the repository so that anyone referencing is able to access is easily. I would start practicing writing the file directory structure for each respository that should have it in the root directory README.md
### File Directory Structure Diagram
```
├── Day 1 - Calorie Counting/
│   ├── day1part1.py
│   ├── day1part2.py
│   ├── raw data.txt
│   └── README.md (Question for Day 1)
├── Day 2 - Rock Paper Scissors/
│   ├── day2part1.py
│   ├── day2part2.py
│   ├── raw data.txt
│   └── README.md (Question for Day 2)
├── Day ... - .../
│   ├── day...part1.py
│   ├── day...part2.py
│   ├── raw data.txt
│   └── README.md (Question for Day ...)
└── file_reader/
│   ├── file_reader.py
│   └── README.md (About file_reader)
└── README.md (This right now!)
```

## Advent of Code 2022 Storyline
Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!