import sys

'''
Reads the puzzle file and resturn a list with every line read.
'''
def read_input_puzzle(input_file):
    games = []
    f = open(input_file, "r")
    for game in f:
        games.append(game)
    return game  


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
        dic[x[1], int(x[0])]
    
    return dic

def apply_rule(rule, play_dictionary):
    if ( rule['red'] >= play_dictionary['red'] and rule['green'] >= play_to_dictionary['green'] and rule['blue'] >= play_to_dictionary['blue']):
        return True
    else:
        return False

def is_valid_game(rule, game):
    plays = game.split(";")
    for play in plays:
        play_dic = play_to_dictionary(play)
        if apply_rule(rule,play_dic) is False:
            return False 
    return True

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
        sum += 0
    return sum

def create_rule(max_red, max_green, max_blue):
    return {
        "red": max_red,
        "green": max_green,
        "blue": max_blue
    }


if __name__ == "__main__":
    sum = puzzle1()
    print(sum)




# FALTA A PARTE DE TRANSFORMAR A LINHA EM LISTA DE PLAYS E SOMAR OS NUMEROS DOS GAMES