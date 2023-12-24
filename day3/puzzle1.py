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

def valid_position(i,j,puzzle_len):
    if i >= 0 and j >= 0 and i < puzzle_len and j < puzzle_len:
        return True
    else:
        return False

def calculate_direct_adjacents(puzzle,i,j, pos):
    puzzle_len = len(puzzle)
    for ii in range(i-1,i+2): # goes from 1 line before to one line ahead
        for jj in range(j-1,j+2):
            if valid_position(ii,jj,puzzle_len):
                #print("(", ii,",", jj,")")
                char = puzzle[ii][jj]
                if not (char.isdigit() or char == "."):
                    pos.append(char)

'''
Goes through all adjacent positions and returns a list with all chars in those positions.
Receives the lines, the line number, first column index and last column index. 
'''
def adjacent_positions(lines, i,fi,li):
    pos = []
    puzzle = parse_lines(lines)
    #number = "" # for debug
    for j in range(fi,li):
        #number += puzzle[i][j] # for debug
        calculate_direct_adjacents(puzzle, i, j, pos)
               
    return pos

def process_number(lines, number, i, index):
    li = index + len(number)
    adjacent_chars = adjacent_positions(lines, i, index, li)
    print(adjacent_chars)
    for char in adjacent_chars:
        if not (char.isdigit() or char == "."):
            print(char + "✅") # for debug
            print(number + "✅") # for debug
            return int(number)
    print(number + "❌") # for debug
    return 0

def find_indexes(line, number):
    indexes = [
        index for index in range(len(line))
        if line.startswith(number, index)
    ]

    return indexes

def process_lines(lines):
    count = 0
    print(lines)
    for i, line in enumerate(lines):
        numbers = re.findall(r'\d+', line)
        print(numbers)
        for number in numbers:
            indexes = find_indexes(line, number)
            print("indexes for number ["+ number + "]: " + str(indexes))
            for index in indexes:
                print("Handling index: " + str(index))
                count += process_number(lines, number, i, index)

    return count

def new_parse_lines(lines):
    puzzle_map = []
    for i, line in enumerate(lines):
        puzzle_line = []
        for j, char in enumerate(line):
            puzzle_line.append(char)
        puzzle_map.append(puzzle_line)
    return puzzle_map, i

def get_number(puzzle_map, puzzle_len,i, j):
    number = puzzle_map[i][j]

    for jj in range(j+1, puzzle_len):
        char = puzzle_map[i][jj]
        if char.isdigit():
            number+=char
        else:
            break
    for jj in range(j-1, -1, -1):
        char= puzzle_map[i][jj]
        if char.isdigit():
            number = char + number

    return int(number) 

def process_symbol(lines, line, column):
    count = 0
    puzzle_map, puzzle_len = new_parse_lines(lines)
    for i in range(line-1,line+2): # goes from 1 line before to one line ahead
        for j in range(column-1,column+2):
            if valid_position(i,j,puzzle_len): # is valid position of a map
                char = puzzle_map[i][j]
                if char.isdigit():
                    number = get_number(puzzle_map,puzzle_len, i, j)
                    print("number: " + str(number))
                    count += number
    return count

def new_process_lines(lines):
    count = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if not (char.isdigit() or char == "."): # symbol, I need to process this
                count += process_symbol(lines,i,j)
    return count
    

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


'''
Function that solves the puzzle.
'''
def puzzle1():
    if len(sys.argv) != 2:
        print("Usage: python3 puzzle1.py puzzle_input")
        sys.exit(1)
    lines = read_input_puzzle(sys.argv[1])
    
    #return process_lines(lines)
    return new_process_lines(lines)

def debug_puzzle1():
    lines = read_input_puzzle("test_input")
    
    return new_process_lines(lines)

if __name__ == "__main__":
    sum = puzzle1()
    #sum = debug_puzzle1()
    print(sum)
