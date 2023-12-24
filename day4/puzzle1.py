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
Extract winning and game numbers from a line. 
'''
def extract_game_numbers(line):
    numbers = line.split(":")[1]
    numbers_splited = numbers.split("|")
    winning_numbers = numbers_splited[0].split()
    game_numbers = numbers_splited[1].split()
    return winning_numbers, game_numbers

'''
Calculate game points from the number of matches between game and winning numbers.
'''
def points(n_matches):
    if n_matches == 0:
        return 0
    
    points = 1
    for _ in range(1, n_matches):
        points *= 2
    
    return points

'''

'''
def process_game(line):
    winning_numbers, game_numbers = extract_game_numbers(line)
    n_matches = 0
    for number in game_numbers:
        if number in winning_numbers:
            n_matches += 1
    
    return points(n_matches)

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
        sum += process_game(line)
    return sum

if __name__ == "__main__":
    sum = puzzle1()
    print(sum)
