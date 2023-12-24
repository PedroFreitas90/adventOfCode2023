import sys
import re


'''
Reads the puzzle file and resturn a list with every line read.
'''
def read_input_puzzle(input_file):
    lines = []
    f = open(input_file, "r")
    for line in f:
        lines.append(line)
    return lines 

def create_color_map(puzzle_len):
    rows = []
    for _ in range(0, puzzle_len):
        columns = ["grey" for _ in range(0,puzzle_len)]
        rows.append(columns)
    return rows

def valid_position(i,j,puzzle_len):
    if i >= 0 and j >= 0 and i < puzzle_len and j < puzzle_len:
        return True
    else:
        return False

def calculate_direct_adjacents(colormap,i,j, pos):
    colormap_len = len(colormap)
    for ii in range(i-1,i+2): # goes from 1 line before to one line ahead
        for jj in range(j-1,j+2):
            if valid_position(ii,jj,colormap_len):
                print("(", ii,",", jj,")")
                colormap[ii][jj]="green"

'''
Goes through all adjacent positions of a number 
'''
def adjacent_positions(lines, i,fi,li):
    pos = []
    puzzle = parse_lines(lines)
    number = "" # for debug
    for j in range(fi,li):
        number += puzzle[i][j] # for debug
        calculate_direct_adjacents(puzzle, i, j, pos)
            
    print(number) #for debug   

    return pos

def find_indexes(line, number):
    indexes = [
        index for index in range(len(line))
        if line.startswith(number, index)
    ]

    return indexes

def process_number(lines, number, i, index):
    li = index + len(number)
    adjacent_chars = adjacent_positions(lines, i, index, li)
    print(adjacent_chars)
    for char in adjacent_chars:
        if not (char.isdigit() or char == "."):
        #print(char + "✅") # for debug
            print(number) # for debug
            return int(number)
    return 0

'''
Parse lines of a puzzle.
'''
def parse_lines(lines):
    puzzle = []
    for _,line in enumerate(lines):
        puzzle_line = []
        for _, char in enumerate(line):
            if char != '\n':
                puzzle_line.append(char)
        puzzle.append(puzzle_line)
    return puzzle 

def process_lines(lines):
    count = 0
    for i, line in enumerate(lines):
        numbers = re.findall(r'\d+', line)
        print(numbers)
        for number in numbers:
            indexes = find_indexes(line, number)
            print(indexes)
            for index in indexes:
                count += process_number(lines, number, i, index)

    return count



'''
Function that solves the puzzle.
'''
def puzzle1():
    if len(sys.argv) != 2:
        print("Usage: python3 puzzle1.py puzzle_input")
        sys.exit(1)
    lines = read_input_puzzle(sys.argv[1])
    
    return process_lines(lines)

if __name__ == "__main__":
    sum = puzzle1()
    print(sum)
