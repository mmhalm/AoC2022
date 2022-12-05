#Advent of Code 2022
from aoc_1 import read_input_file
TASKNUMBER=4


def task_4(input):
    duplicates = 0
    for i in input:
        #print(i)
        elf_1 = i.split(",")[0]
        elf_2 = i.split(",")[1]

        elf_1_start = int(elf_1.split('-')[0])
        elf_1_end = int(elf_1.split('-')[1])
        elf_2_start = int(elf_2.split('-')[0])
        elf_2_end = int(elf_2.split('-')[1])

        if (elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) or (elf_2_start <= elf_1_start and elf_2_end >= elf_1_end):
            print(i)
            duplicates += 1
    
    print("duplicates: ", duplicates)

def task_4_1(input):
    overlaps = 0
    for i in input:
        #print(i)
        elf_1 = i.split(",")[0]
        elf_2 = i.split(",")[1]

        elf_1_start = int(elf_1.split('-')[0])
        elf_1_end = int(elf_1.split('-')[1])
        elf_2_start = int(elf_2.split('-')[0])
        elf_2_end = int(elf_2.split('-')[1])

        if (elf_1_start <= elf_2_start <= elf_1_end) or (elf_1_start <= elf_2_end <= elf_1_end) or (elf_2_start <= elf_1_start <= elf_2_end) or (elf_2_start <= elf_1_end <= elf_2_end):
            print(i)
            overlaps += 1
    
    print("overlapping: ", overlaps)


def main():
    input = read_input_file(TASKNUMBER)
    #print(input)
    task_4_1(input)

if __name__ == "__main__":
    main()