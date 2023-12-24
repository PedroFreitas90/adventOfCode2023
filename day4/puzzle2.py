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
def extract_game_numbers(numbers):
    numbers_splited = numbers.split("|")
    winning_numbers = numbers_splited[0].split()
    game_numbers = numbers_splited[1].split()
    return winning_numbers, game_numbers

'''
Calculates the number of game numbers that are also on winning numbers.
'''
def calculate_n_matches(numbers):
    winning_numbers, game_numbers = extract_game_numbers(numbers)
    n_matches = 0
    for number in game_numbers:
        if number in winning_numbers:
            n_matches += 1
    return n_matches

'''
Creates a game dictionary where the keys are the game number and the values the number of matching numbers.
'''
def game_dictionary(lines):
    games_dic = {}
    for line in lines:
        game_key, numbers = line.split(":")
        key = int(game_key.split()[1])
        games_dic[key] = calculate_n_matches(numbers)
    return games_dic

'''
Aplies recursivity on the each game to calculate how many copies they are generating.
'''
def card_tree(card_number, game_dictionary):
    
    n_matches = game_dictionary[card_number]
    number_of_copies = n_matches
    for i in range(0, n_matches):
        next_card = card_number + 1 + i
        number_of_copies += card_tree(next_card, game_dictionary)
    return number_of_copies

'''
Calculate the number of original cards.
'''
def original_cards(game_dictionary):
    i = 0
    for _ in game_dictionary.keys():
        i += 1
    return i


'''
Function that solves the puzzle.
'''
def puzzle1():
    if len(sys.argv) != 2:
        print("Usage: python3 puzzle1.py puzzle_input")
        sys.exit(1)
    lines = read_input_puzzle(sys.argv[1])
    game_dic = game_dictionary(lines)

    sum = original_cards(game_dic)

    for key in game_dic.keys():
        sum += card_tree(key, game_dic)
    return sum

if __name__ == "__main__":
    sum = puzzle1()
    print(sum)
