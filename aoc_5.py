#Advent of Code 2022
from aoc_1 import read_input_file
TASKNUMBER=5


def crane(howmany, fromwhere, towhere):
    box_from = array_dict[fromwhere]
    box_to = array_dict[towhere]

    for i in range(0,howmany):
        box_to.append(box_from.pop(-1))
    
    array_dict[fromwhere] = box_from
    array_dict[towhere] = box_to

def crane_9001(howmany, fromwhere, towhere):
    box_from = array_dict[fromwhere]
    box_to = array_dict[towhere]

    moving_boxes = box_from[(-1*howmany):]
    for i in moving_boxes:
        box_to.append(i)
    
    array_dict[fromwhere] = box_from[:(-1*howmany)]
    array_dict[towhere] = box_to


def task_5(input):
    
    global array_dict
    array_dict = {'1':['S','C','V','N'],
                '2':['Z','M','J','H','N','S'],
                '3':['M','C', 'T', 'G', 'J', 'N', 'D'], 
                '4':['T', 'D', 'F', 'J', 'W', 'R', 'M'],
                '5':['P', 'F', 'H'],
                '6':['C', 'T', 'Z', 'H', 'J'],
                '7':['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
                '8':['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
                '9':['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']
    }

    for i in input:
        how_many = int(i.split(' ')[1])
        from_where = i.split(' ')[3]
        to_where = i.split(' ')[5]

        #crane(how_many, from_where, to_where)
        crane_9001(how_many, from_where, to_where)

    result = ""
    for j in array_dict.values():
        print(j[-1])
        result = result + j[-1]

    print(result)




def main():
    input = read_input_file(TASKNUMBER)
    input = input[10:]    
    task_5(input)

if __name__ == "__main__":
    main()