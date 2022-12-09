import sys
import os
sys.path.insert(0, r"./file_reader")    #import file_reader function from file_reader/file_reader.py

from file_reader import file_reader

FILE: str = r"raw data.txt"
CURRENT_WORKING_DIRECTORY: str = os.path.dirname(os.path.abspath(__file__))


def main():
    datastream_buffer: str = file_reader(CURRENT_WORKING_DIRECTORY + r"/" + FILE)

    NO_OF_REPEAT: int = 4

    start_of_packet_marker_position: int = 0
    for position in range(len(datastream_buffer)-NO_OF_REPEAT):
        if len(set(datastream_buffer[position:position+NO_OF_REPEAT])) == NO_OF_REPEAT:
            start_of_packet_marker_position = position + NO_OF_REPEAT
            break
    
    print(f"{start_of_packet_marker_position} characters need to be processed before the first start-of-packet marker is detected")

if __name__ == "__main__":
    main()