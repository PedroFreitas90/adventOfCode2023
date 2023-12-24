import sys
import re

seeds = []
seed_to_soil_dic = {}
soil_to_fertilizer_dic = {}
fertilizer_to_water_dic = {}
water_to_light_dic = {}
light_to_temperature_dic = {}
temperature_to_humidity_dic = {}
humidity_to_location_dic = {}

seed_to_soil_list = []
soil_to_fertilizer_list = []
fertilizer_to_water_list = []
water_to_light_list = []
light_to_temperature_list = []
temperature_to_humidity_list = []
humidity_to_location_list = []

def line_to_dic(line, dic):
    #print(line)
    start_dest, start_source, interval = line.split()
    for i in range(0, int(interval)):
        dic[int(start_source)+ i] = int(start_dest) + i

def process_lines(lines):
    key_line_pattern = re.compile(r'^(seeds:|seed-to-soil map:|soil-to-fertilizer map:|fertilizer-to-water map:|water-to-light map:|light-to-temperature map:|temperature-to-humidity map:|humidity-to-location map:)')
    for line in lines:
        if(re.match(key_line_pattern, line)):
            key = line.split(":")[0]
            #print(key)
            if (key == "seeds"):
                for seed in line.split(":")[1].split():
                    seeds.append(int(seed))
        else:
            if (key == "seed-to-soil map"):
                #line_to_dic(line, seed_to_soil_dic)
                seed_to_soil_list.append(line)
            elif (key == "soil-to-fertilizer map"):
                #line_to_dic(line,soil_to_fertilizer_dic)
                soil_to_fertilizer_list.append(line)
            elif (key == "fertilizer-to-water map"):
                #line_to_dic(line,fertilizer_to_water_dic)
                fertilizer_to_water_list.append(line)
            elif (key == "water-to-light map"):
                #line_to_dic(line,water_to_light_dic)
                water_to_light_list.append(line)
            elif (key == "light-to-temperature map"):
                #line_to_dic(line,light_to_temperature_dic)
                light_to_temperature_list.append(line)
            elif (key == "temperature-to-humidity map"):
                #line_to_dic(line,temperature_to_humidity_dic)
                temperature_to_humidity_list.append(line)
            elif (key == "humidity-to-location map"):
                #line_to_dic(line,humidity_to_location_dic)
                humidity_to_location_list.append(line)

def get_value_from_dic(dic, key):
    try:
        value = dic[key]
        return value
    except:
        return key

def get_value_from_list(list, key):
    value = key
    for line in list:
        start_dest, start_source, interval = map(int, line.split())
        if key >= start_source and key < start_source + interval: # the key is in the range
            value = key - start_source + start_dest
    return value

def calculate_seeds_dic():
    seeds_dic = {}
    '''
    seed_to_soil_dic: seed -> soil  
    soil_to_fertilizer_dic: soil -> fertilizer 
    fertilizer_to_water_dic: fertilizer -> water 
    water_to_light_dic: water -> light
    light_to_temperature_dic: light -> temperature 
    temperature_to_humidity_dic: temperature -> humidity 
    humidity_to_location_dic: humidity -> location
    soil -> fertilizer
    '''
    for seed in seeds:
        #print("SEED: " + str(seed))
        soil = get_value_from_dic(seed_to_soil_dic, seed ); fertilizer = get_value_from_dic(soil_to_fertilizer_dic, soil)
        water = get_value_from_dic(fertilizer_to_water_dic, fertilizer); light = get_value_from_dic(water_to_light_dic, water)
        temperature = get_value_from_dic(light_to_temperature_dic, light)
        humidity = get_value_from_dic(temperature_to_humidity_dic, temperature) 
        location = get_value_from_dic(humidity_to_location_dic, humidity)
        entry = {
            "soil": soil,
            "fertilizer": fertilizer,
            "water": water,
            "temperature": temperature,
            "humidity": humidity,
            "location": location
        }   
        seeds_dic[seed] = entry
    return seeds_dic

def calculate_seeds_dic_from_list():
    seeds_dic = {}
    '''
    seed_to_soil_dic: seed -> soil  
    soil_to_fertilizer_dic: soil -> fertilizer 
    fertilizer_to_water_dic: fertilizer -> water 
    water_to_light_dic: water -> light
    light_to_temperature_dic: light -> temperature 
    temperature_to_humidity_dic: temperature -> humidity 
    humidity_to_location_dic: humidity -> location
    soil -> fertilizer
    '''
    for seed in seeds:
        #print("SEED: " + str(seed))
        soil = get_value_from_list(seed_to_soil_list, seed ); fertilizer = get_value_from_list(soil_to_fertilizer_list, soil)
        water = get_value_from_list(fertilizer_to_water_list, fertilizer); light = get_value_from_list(water_to_light_list, water)
        temperature = get_value_from_list(light_to_temperature_list, light)
        humidity = get_value_from_list(temperature_to_humidity_list, temperature) 
        location = get_value_from_list(humidity_to_location_list, humidity)
        entry = {
            "soil": soil,
            "fertilizer": fertilizer,
            "water": water,
            "temperature": temperature,
            "humidity": humidity,
            "location": location
        }   
        seeds_dic[seed] = entry
    return seeds_dic

def read_input_puzzle(input_file):
    lines = []
    f = open(input_file, "r")
    for line in f:
        if line != "\n":
            lines.append(line)
    return lines

def calculate_minimum_location(seeds_dic):
    minimum_location = sys.maxsize
    for seed in seeds_dic:
        location = seeds_dic[seed]['location'] 
        if location < minimum_location:
            minimum_location = location
    return location


'''
Function that solves the puzzle.
'''
def puzzle1():
    if len(sys.argv) != 2:
        print("Usage: python3 puzzle1.py puzzle_input")
        sys.exit(1)
    lines = read_input_puzzle(sys.argv[1])
    process_lines(lines)

    #debug_dic()

    #puzzle_dic = build_puzzle_dic()
    seeds_dic = calculate_seeds_dic_from_list()
    #print(seeds_dic)
    lowest = calculate_minimum_location(seeds_dic)
    return lowest

if __name__ == "__main__":
    lowest = puzzle1()
    print(lowest)
