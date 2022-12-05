# Advent of code 2022
TASKNUMBER="1-1"


def read_input_file(tasknumber):
    my_file = open(f"{tasknumber}.txt", "r")
    input = my_file.read().splitlines()
    return input

def task_1_1(input):
    cals = 0
    elf_dict = {} 
    number = 1
    for i in input:
        if i != "":
            cals += int(i)
        elif i == "":
            elf_dict[number] = cals
            number += 1
            cals = 0
    return elf_dict

def find_max_cals(elf_dict):
    max_value = max(elf_dict.values())
    max_key = max(elf_dict, key=elf_dict.get)
    return (max_key, max_value)

def main():
    input = read_input_file(TASKNUMBER)
    elf_dictionary = task_1_1(input)

    elf_1 = find_max_cals(elf_dictionary)
    elf_dictionary.pop(elf_1[0])
    elf_2 = find_max_cals(elf_dictionary)
    elf_dictionary.pop(elf_2[0])
    elf_3 = find_max_cals(elf_dictionary)

    total = int(elf_1[1]) + int(elf_2[1] + int(elf_3[1]))
    print(total) 


if __name__ == "__main__":
    main()