import sys

'''
For each game get the minimum number of each color cube to make that game possible:
    - Check the biggest value of each cube in every play of one game
Multiple the number of each minimum cube number and get the power. 

Then sum all the powers.
'''



'''
Reads the puzzle file and resturn a list with every line read.
'''
def read_input_puzzle(input_file):
    games = []
    f = open(input_file, "r")
    for game in f:
        games.append(game)
    return games


'''
Receives a play of a game and transform it in a dictionary.
'''
def play_to_dictionary(play):
    balls = play.split(",")
    dic = {
        "red": 0,
        "green": 0, 
        "blue": 0
    }
    
    for ball in balls:
        x = ball.split() # -> 3 blue -> ["3", "blue"]
        dic[x[1]] = int(x[0])
    
    return dic

'''
Calculates the power of a dictionary.
'''
def calculate_dictionary_power(power_dictionary):
    return power_dictionary['red'] * power_dictionary['green'] * power_dictionary['blue']

'''
Update a power dictionary with a play dictionary, if any play dictionary value is bigger that the power dictionary value.
'''
def update_power_dictionary(power_dictionary, play_dic):
    if power_dictionary['red'] < play_dic['red']:
        power_dictionary['red'] = play_dic['red']
    if power_dictionary['green'] < play_dic['green']:
        power_dictionary['green'] = play_dic['green']
    if power_dictionary['blue'] < play_dic['blue']:
        power_dictionary['blue'] = play_dic['blue']
    return power_dictionary

'''
Receives a string with the plays of the game and return the power of each game
'''
def calculate_game_power(game):
    plays = game.split(";")
    power_dictionary = {
        "red": 0,
        "green": 0, 
        "blue": 0
    }
    for play in plays:
        play_dic = play_to_dictionary(play)
        power_dictionary = update_power_dictionary(power_dictionary, play_dic)
    
    return calculate_dictionary_power(power_dictionary)

'''
Receives a full game line and returns the string with the plays of the game.
'''
def strip_game(game):
    game_plays = game.split(":")[1] 
    return game_plays

'''
Function that solves the puzzle.
'''
def puzzle2():
    if len(sys.argv) != 2:
        print("Usage: python3 puzzle2.py puzzle_input")
        sys.exit(1)
    
    games = read_input_puzzle(sys.argv[1])
    
    sum = 0
    for game in games:
        game_plays = strip_game(game)
        
        sum += calculate_game_power(game_plays)
    return sum

if __name__ == "__main__":
    sum = puzzle2()
    print(sum)
