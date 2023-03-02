with open('2205_input.txt') as input_file:
    input = input_file.readlines()

stacks = [[] for n in range(0,9)]

# get crates
for line in input:
    if (line[0] == " " or line[0] == "[") and line[1] != "1":
        stacks[0].append(line[1])
        stacks[1].append(line[5])
        stacks[2].append(line[9])
        stacks[3].append(line[13])
        stacks[4].append(line[17])
        stacks[5].append(line[21])
        stacks[6].append(line[25])
        stacks[7].append(line[29])
        stacks[8].append(line[33])
    else:
        break

# eliminate 'blank crates' from stacks
for index, stack in enumerate(stacks, 0):
    stacks[index] = [x for x in stack if x != " "]

# crate-moving section
for line in input:
    if line[0] == "m":
        # get number of crates to move, and the crates' original and final stacks
        line = line.split(" ")
        pick = int(line[1])
        origin = int(line[3])
        destination = int(line[5])
        
        # 'transfer' crate between stacks
        for n in range(0, pick):
            crate = stacks[origin-1][0]
            stacks[origin-1].pop(0)
            stacks[destination-1].insert(0,crate)

stack_tops = ""

for stack in stacks:
    stack_tops += stack[0]

print(stack_tops)