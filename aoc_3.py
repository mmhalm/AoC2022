#Advent of Code 2022
from aoc_1 import TASKNUMBER, read_input_file
TASKNUMBER=3



def find_priority(char):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorities = {}
    j = 1
    for i in chars:
        priorities[i] = j
        j += 1
    return priorities[char]


def task_3(input):
    total_score = 0
    for i in range(0,len(input)-2):
        if i%3 == 0 or i == 0:
            common_item = ""
            # len(i) on parillinen aina
            elf_1 = input[i]
            elf_2 = input[i+1]
            elf_3 = input[i+2]
            
            #comp_2 = i[(len(i)//2):]

            #for j in comp_1:
            #    if j in comp_2:
            #        common_item = j

            for j in elf_1:
                if j in elf_2:
                    if j in elf_3:
                        common_item = j

            # assuming len(common_item) == 1
            score = find_priority(common_item)
            total_score += score
            print(total_score, common_item)
    print(total_score)
        


def main():
    input = read_input_file(TASKNUMBER)
    task_3(input)

if __name__ == "__main__":
    main()