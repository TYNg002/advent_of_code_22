# create list of rucksacks
with open('2203_input.txt') as input_file:
    rucksacks_all = input_file.readlines()

# string of items in priority order, where the index of each item is its priority
items = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_total = 0

# loop for each rucksack
for rucksack in rucksacks_all:
    rucksack = rucksack.strip("\n")
    total_items = len(rucksack)

    # separate first and second half of all items in rucksack
    compartment1 = rucksack[:int(total_items/2)]
    compartment2 = rucksack[int(total_items/2):]

    # get the common item between both compartments
    error_item = "".join(set(compartment1) & set(compartment2))
    # get the priority of the item by referencing the 'items' variable
    priority = items.index(error_item)
    # add to priority total
    priority_total += priority

print(priority_total)
