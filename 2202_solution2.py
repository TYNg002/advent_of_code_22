# create list of rounds
with open('2202_input.txt') as input_file:
    game = input_file.readlines()

running_total = 0

# loop for each round
for round in game:
    # make each round a list where the first and second items are 
    # the opponent's chosen shape, and round outcome respectively
    selections = round.strip("\n").split(" ")

    # add score to running total based on round outcome
    if selections[1] == "X":
        pass
    elif selections[1] == "Y":
        running_total += 3
    else:
        running_total += 6

    # add score to running total based on chosen shape
    if selections[1] == "X":
        if selections[0] == "A":
            running_total += 3
        elif selections[0] == "B":
            running_total += 1
        else:
            running_total += 2
    elif selections[1] == "Y":
        if selections[0] == "A":
            running_total += 1
        elif selections[0] == "B":
            running_total += 2
        else:
            running_total += 3
    else:
        if selections[0] == "A":
            running_total += 2
        elif selections[0] == "B":
            running_total += 3
        else:
            running_total += 1

print(running_total)