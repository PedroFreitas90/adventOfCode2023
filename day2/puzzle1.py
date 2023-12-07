import sys

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
Apply a rule in a play of a game.
'''
def apply_rule(rule, play_dictionary):
    if ( rule['red'] >= play_dictionary['red'] and rule['green'] >= play_dictionary['green'] and rule['blue'] >= play_dictionary['blue']):
        return True
    else:
        return False

'''
Receives a rule and the string with the plays of the game and checks if each play is valid.
'''
def is_valid_game(rule, game):
    plays = game.split(";")
    for play in plays:
        play_dic = play_to_dictionary(play)
        if apply_rule(rule,play_dic) is False:
            return False 
    return True

'''
Receives a full game line and returns the number of the game as well the string with the plays of the game.

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green --> 1 , (3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green)
'''
def strip_game(game):
    game_number, game_plays = game.split(":")[0], game.split(":")[1]
    number = game_number.split()[1] 
    return int(number), game_plays

'''
Creates a rule with the max cubes of each color.
'''
def create_rule(max_red, max_green, max_blue):
    return {
        "red": max_red,
        "green": max_green,
        "blue": max_blue
    }

'''
Function that solves the puzzle.
'''
def puzzle1():
    if len(sys.argv) != 5:
        print("Usage: python3 puzzle1.py puzzle_input max_red_cubes max_green_cubes max_blue_cubes")
        sys.exit(1)
    
    games = read_input_puzzle(sys.argv[1])
    rule = create_rule(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    
    sum = 0
    for game in games:
        game_number, game_plays = strip_game(game)
        if is_valid_game(rule, game_plays):
            sum += game_number
    return sum




if __name__ == "__main__":
    sum = puzzle1()
    print(sum)
