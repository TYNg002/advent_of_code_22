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

    # check if one list is within another list by comparing start and end numbers
    if int(pair_list[0][0]) <= int(pair_list[1][0]) and int(pair_list[0][1]) >= int(pair_list[1][1]):
        pairs_total += 1
    elif int(pair_list[0][0]) >= int(pair_list[1][0]) and int(pair_list[0][1]) <= int(pair_list[1][1]):
        pairs_total += 1

print(pairs_total)