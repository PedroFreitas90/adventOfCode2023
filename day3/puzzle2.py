import sys

number_dic = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}


'''
Returns a list with all numbers spelled.
'''
def get_spelled_numbers():
    spelled_numbers = ['one','two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    return spelled_numbers

'''
Returns a list with all numbers spelled reversed.
'''
def get_reversed_spelled_numbers():
    spelled_numbers =  get_spelled_numbers()
    reversed_spelled_numbers = []
    for number in spelled_numbers:
        reversed_spelled_numbers.append(reverse_str(number))
    return reversed_spelled_numbers

'''
Reverse a string.
'''
def reverse_str(input_string):
    reversed_str = "".join(reversed(input_string))

    return reversed_str

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
Find the first index of the first number spelled
'''
def find_index_first_spelled_number(line):
    first_occurrence = sys.maxsize
    first_number = ""
    # goes through 
    for number in get_spelled_numbers():
        index = line.find(number)
        if index != -1 and index < first_occurrence:
            first_occurrence = index
            first_number = number
    #print("[ find_index_first_spelled_number] first_occurence: " + str(first_occurrence))
    #print("[ find_index_first_spelled_number] first_number: " + first_number)
    return first_occurrence, first_number

'''
Find the first index of the last number spelled
'''
def find_index_last_spelled_number(line):
    last_occurrence = -1
    last_number = ""
    # goes through the reversed spelled numbers list and try to find each one 
    for number in get_spelled_numbers():
        try:
            index = line.rindex(number)
            if index != -1 and index > last_occurrence: # if the substring exists and if it's the major index 
                last_occurrence = index
                last_number = number
        except:
            pass
    #print("[ find_index_last_spelled_number] last_occurence: " + str(last_occurrence))
    #print("[ find_index_last_spelled_number] last_number: " + last_number)
    return last_occurrence, last_number


def spelled_to_char(number):
    return number_dic[number]

'''
Goes through every char in the line and returns the first digit.
'''
def extract_first_number(line):
    index = sys.maxsize
    number = "0"
    for i,char in enumerate(line): 
        if char.isdigit() and i < index:
            index = i; number = char
    fi,fn = find_index_first_spelled_number(line)
    if fi != -1 and index != -1 and fi < index:
        return spelled_to_char(fn)
    else:
        return number

'''
Goes through every char in the reversed line and returns the first digit, which corresponds to the last digit in the normal line.
'''
def extract_last_number(line):
    index = sys.maxsize
    number = "0"
    
    reversed_line = reverse_str(line)
    for i,char in enumerate(reversed_line): 
        if char.isdigit() and i < index:
            index = i; number = char
    
    index = len(line) - 1 - index

    li,ln = find_index_last_spelled_number(line)
        
    if li != -1 and li > index and index != -1:
        return spelled_to_char(ln)
    else:
        return number

'''
Extract the first and last digit of each line and returns as a int.
'''
def extract_number_of_line(line):
    fn = extract_first_number(line)
    ln = extract_last_number(line)
    number = fn + ln #concatenation of first and last number
    return int(number)

'''
Function that solves the puzzle.
'''
def puzzle2():
    if len(sys.argv) != 2:
        print("Usage: python3 puzzle2.py puzzle_input")
        sys.exit(1)
    
    lines = read_input_puzzle(sys.argv[1])
    
    sum = 0
    for line in lines:
        sum += extract_number_of_line(line)
    return sum

if __name__ == "__main__":
    sum = puzzle2()
    print(sum)
