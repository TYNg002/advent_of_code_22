# open input file and store as string
with open("2201_input.txt") as calorie_file:
    calorie_string = calorie_file.read()

# calories_grouped returns a list in which each item is a string of calories per elf
calories_grouped = calorie_string.split("\n\n")

# set default maximum values
max_calories = [0, 0, 0]

# loop for each elf's stash
for group_string in calories_grouped:
    # reset elf's total calories for each loop
    elf_calories = 0
    # create list of calories in the stash
    group_list = group_string.split("\n")
    # add each item's calories to the elf's total
    for item in group_list:
        elf_calories += int(item)
    # set the elf's total as a maximum if it exceeds the any current maximums
    if elf_calories > max_calories[0]:
        # 'bump' the maximum value to the next maximum variable if 
        # the value of one maximum variable is replaced
        if max_calories[0] != 0:
            if max_calories[1] != 0:
                max_calories[2] = max_calories[1]
            max_calories[1] = max_calories[0]
        max_calories[0] = elf_calories
    elif elf_calories > max_calories[1]:
        if max_calories[1] != 0:
            max_calories[2] = max_calories[1]
        max_calories[1] = elf_calories
    elif elf_calories > max_calories[2]:
        max_calories[2] = elf_calories
    print(elf_calories)
    print(max_calories)

total_max = 0

for max in max_calories:
    total_max += max

print(total_max)