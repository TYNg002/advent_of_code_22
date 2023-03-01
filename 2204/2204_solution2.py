# create list of pairs
with open('2204_input.txt') as input_file:
    pairs_all = input_file.readlines()

pairs_total = 0

# loop for each pair
for pair_string in pairs_all:
    # get pairs in string form
    pair_string = pair_string.strip("\n")
    # get pairs in list form
    pair_list = pair_string.split(",")

    # amend pair_list so each pair is a list of start and end numbers
    for index, assignment_string in enumerate(pair_list, 0):
        pair_list[index] = assignment_string.split("-")
        
        # set each assignment to a different variable as a range
        if index == 0:
            assignment1 = range(int(pair_list[0][0]), int(pair_list[0][1])+1)
        else:
            assignment2 = range(int(pair_list[1][0]), int(pair_list[1][1])+1)
    
    # increase count if there is overlap between the assignments
    if set(assignment1) & set(assignment2):
        pairs_total += 1

print(pairs_total)
