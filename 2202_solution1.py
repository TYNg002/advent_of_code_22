# create list of rounds
with open('2202_input.txt') as input_file:
    game = input_file.readlines()

running_total = 0

# loop for each round
for round in game:
    # make each round a list where the first and second items are 
    # the opponent's chosen shape, and the player's chosen shape respectively
    selections = round.strip("\n").split(" ")

    # add score to running total based on chosen shape
    if selections[1] == "X":
        running_total += 1
    elif selections[1] == "Y":
        running_total += 2
    else:
        running_total += 3

    # add score to running total based on round outcome
    if selections[0] == "A":
        if selections[1] == "X":
            running_total += 3
        elif selections[1] == "Y":
            running_total += 6
        else:
            pass
    elif selections[0] == "B":
        if selections[1] == "X":
            pass
        elif selections[1] == "Y":
            running_total += 3
        else:
            running_total += 6
            
    else:
        if selections[1] == "X":
            running_total += 6
        elif selections[1] == "Y":
            pass
        else:
            running_total += 3

print(running_total)