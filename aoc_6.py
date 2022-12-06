# Advent of Code 2022
# 6

with open('6.txt', 'r') as input_file:
    input = input_file.read()
    #print(input)

for i in range(0,len(input)):
    substring = input[i:i+14]
    set_substring = set(substring)
    #print(substring, set_substring)
    
    if len(substring) == len(set_substring):
        print(substring, i+14)
        break