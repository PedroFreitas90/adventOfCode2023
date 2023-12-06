import sys

'''
Reads the puzzle file and resturn a list with every line read.
'''
def read_input_puzzle(input_file):
    lines = []
    f = open(input_file, "r")
    for line in f:
        lines.append(line)
    return lines 

'''
Goes through every char in the line and returns the first digit.
'''
def extract_first_number(line):
    for _,char in enumerate(line): 
        if char.isdigit():
            return char
    return 0

'''
Goes through every char in the reversed line and returns the first digit, which corresponds to the last digit in the normal line.
'''
def extract_last_number(line):
    reversed_line = "".join(reversed(line))
    for _,char in enumerate(reversed_line):
        if char.isdigit():
            return char
    return 0

'''
Extract the first and last digit of each line and returns as a int.
'''
def extract_number_of_line(line):
    number = extract_first_number(line) + extract_last_number(line) #concatenation of first and last number 
    return int(number)

'''
Function that solves the puzzle.
'''
def puzzle1():
    if len(sys.argv) != 2:
        print("Usage: python3 puzzle1.py puzzle_input")
        sys.exit(1)
    lines = read_input_puzzle(sys.argv[1])
    sum = 0
    for line in lines:
        sum += extract_number_of_line(line)
    return sum

if __name__ == "__main__":
    sum = puzzle1()
    print(sum)
