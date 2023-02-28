# open input file and store as string
with open("2201_input.txt") as calorie_file:
    calorie_string = calorie_file.read()

# calories_grouped returns a list in which each item is a string of calories per elf
calories_grouped = calorie_string.split("\n\n")

max_calories = 0

# loop for each elf's stash
for group_string in calories_grouped:
    # reset elf's total calories for each loop
    elf_calories = 0
    # create list of calories in the stash
    group_list = group_string.split("\n")
    # add each item's calories to the elf's total
    for item in group_list:
        elf_calories += int(item)
    # set the elf's total as the maximum if it exceeds the current maximum
    if elf_calories > max_calories:
        max_calories = elf_calories

print(max_calories)