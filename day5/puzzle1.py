import sys
import re

def read_input_puzzle(input_file):
    lines = []
    f = open(input_file, "r")
    for line in f:
        if line != "\n":
            lines.append(line)
    return lines

seeds = []
seed_to_soil_list = []
soil_to_fertilizer_list = []
fertilizer_to_water_list = []
water_to_light_list = []
light_to_temperature_list = []
temperature_to_humidity_list = []
humidity_to_location_list = []

def process_lines(lines):
    key_line_pattern = re.compile(r'^(seeds:|seed-to-soil map:|soil-to-fertilizer map:|fertilizer-to-water map:|water-to-light map:|light-to-temperature map:|temperature-to-humidity map:|humidity-to-location map:)')
    for line in lines:
        if(re.match(key_line_pattern, line)):
            key = line.split(":")[0]
            if (key == "seeds"):
                for seed in line.split(":")[1].split():
                    seeds.append(int(seed))
        else:
            line = line.strip("\n")
            if (key == "seed-to-soil map"):
                seed_to_soil_list.append(line)
            elif (key == "soil-to-fertilizer map"):
                soil_to_fertilizer_list.append(line)
            elif (key == "fertilizer-to-water map"):
                fertilizer_to_water_list.append(line)
            elif (key == "water-to-light map"):
                water_to_light_list.append(line)
            elif (key == "light-to-temperature map"):
                light_to_temperature_list.append(line)
            elif (key == "temperature-to-humidity map"):
                temperature_to_humidity_list.append(line)
            elif (key == "humidity-to-location map"):
                humidity_to_location_list.append(line)

def get_value_from_list(list, key):
    value = key
    for line in list:
        start_dest, start_source, interval = map(int, line.split())
        if key >= start_source and key < start_source + interval: # the key is in the range   
            value = key - start_source + start_dest
            break
    return value

def calculate_seeds_dic_from_list():
    seeds_dic = {}

    for seed in seeds:
        soil = get_value_from_list(seed_to_soil_list, seed ); fertilizer = get_value_from_list(soil_to_fertilizer_list, soil)
        water = get_value_from_list(fertilizer_to_water_list, fertilizer); light = get_value_from_list(water_to_light_list, water)
        temperature = get_value_from_list(light_to_temperature_list, light)
        humidity = get_value_from_list(temperature_to_humidity_list, temperature) 
        location = get_value_from_list(humidity_to_location_list, humidity)  
        seeds_dic[seed] = location
    return seeds_dic


def calculate_minimum_location(seeds_dic): 
    locations = [seeds_dic[seed] for seed in seeds_dic]
    return min(locations)


'''
Function that solves the puzzle.
'''
def puzzle1():
    if len(sys.argv) != 2:
        print("Usage: python3 puzzle1.py puzzle_input")
        sys.exit(1)
    lines = read_input_puzzle(sys.argv[1])
    process_lines(lines)

    seeds_dic = calculate_seeds_dic_from_list()

    lowest = calculate_minimum_location(seeds_dic)
    return lowest

if __name__ == "__main__":
    lowest = puzzle1()
    print(lowest)
