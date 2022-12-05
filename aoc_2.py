# Advent of Code 2022
# 2
from aoc_1 import read_input_file
TASKNUMBER = "2"

def shape_score(shape):
    if shape == "Y": # paper
        return 2
    elif shape == "X":  # rock
        return 1
    elif shape == "Z": # scissors
        return 3

def outcome_score(o_shape, y_shape):
    if o_shape == "A":  # rock
        if y_shape == "Y":
            return 6
        elif y_shape == "Z":
            return 0
        elif y_shape == "X":
            return 3
    elif o_shape == "B":  # paper
        if y_shape == "Y": # paper
            return 3
        elif y_shape == "Z": #scissors
            return 6
        elif y_shape == "X": # rock
            return 0
    elif o_shape == "C":  # scissors
        if y_shape == "Y": # paper
            return 0
        elif y_shape == "Z": #scissors
            return 3
        elif y_shape == "X": # rock
            return 6

def task_2(input):
    total_score = 0
    for i in input:
        opponent, you = i.split(" ")
        s_score = shape_score(you)
        o_score = outcome_score(opponent, you)
        score = s_score + o_score
        total_score += score
    print (total_score)

def outcome_2(outcome):
    outcomes = {"X":0,
                "Y":3,
                "Z":6 
    }
    return outcomes[outcome]

def shape_2(o_shape, outcome):
    if outcome == "X": # lose
        if o_shape == "A": # rock
            return shape_score("Z") #sci
        elif o_shape == "B": #paper
            return shape_score("X") # rock
        elif o_shape == "C": #scissors
            return shape_score("Y") # paper
    elif outcome == "Y": #draw
        if o_shape == "A": # rock
            return shape_score("X")
        elif o_shape == "B": #paper
            return shape_score("Y") 
        elif o_shape == "C": #scissors
            return shape_score("Z")
    elif outcome == "Z": # win
        if o_shape == "A": # rock
            return shape_score("Y") #paper
        elif o_shape == "B": #paper
            return shape_score("Z") #sci
        elif o_shape == "C": #scissors
            return shape_score("X") # rock


def task_2_2(input: list):
    total_score = 0
    for i in input:
        opponent, outcome = i.split(" ")
        o_score = outcome_2(outcome)
        s_score = shape_2(opponent, outcome)
        score = o_score + s_score 
        total_score += score
    print(total_score)   

def main():
    input = read_input_file(TASKNUMBER)
    task_2_2(input)

if __name__ == "__main__":
    main()