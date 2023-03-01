# create list of rucksacks
with open('2203_input.txt') as input_file:
    rucksacks_all = input_file.readlines()

# string of items in priority order, where the index of each item is its priority
items = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_total = 0

# loop for each rucksack
for rucksack_number, rucksack in enumerate(rucksacks_all,1):
    rucksack = rucksack.strip("\n")

    # if rucksack is number 3 (or a multiple of 3)
    if rucksack_number % 3 == 0:
        rucksack3 = rucksack
        # get the common item between 3 rucksacks
        badge = "".join(set(rucksack3) & set(rucksack2) & set(rucksack1))
        # get the priority of the item by referencing the 'items' variable
        priority = items.index(badge)
        # add to priority total
        priority_total += priority

    # if rucksack is the second of a set of 3 rucksacks
    elif rucksack_number % 2 == 0:
        rucksack2 = rucksack

    # if rucksack is the first of a set of 3 rucksacks
    else:
        rucksack1 = rucksack

print(priority_total)
