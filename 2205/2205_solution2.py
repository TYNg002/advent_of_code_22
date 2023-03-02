with open('2205_input.txt') as input_file:
    input = input_file.readlines()

stacks = ["" for n in range(0,9)]

# get crates
for line in input:
    if (line[0] == " " or line[0] == "[") and line[1] != "1":
        stacks[0] += (line[1])
        stacks[1] += (line[5])
        stacks[2] += (line[9])
        stacks[3] += (line[13])
        stacks[4] += (line[17])
        stacks[5] += (line[21])
        stacks[6] += (line[25])
        stacks[7] += (line[29])
        stacks[8] += (line[33])
    else:
        break

# eliminate 'blank crates' from stacks
for index, stack in enumerate(stacks, 0):
    stacks[index] = stacks[index].strip(" ")

# crate-moving section
for line in input:
    if line[0] == "m":
        # get number of crates to move, and the crates' original and final stacks
        line = line.split(" ")
        pick = int(line[1])
        origin = int(line[3])
        destination = int(line[5])

        # 'transfer' crate(s) between stacks
        crate = stacks[origin-1][:pick]
        stacks[origin-1] = stacks[origin-1][pick:]
        stacks[destination-1] = crate + stacks[destination-1]

stack_tops = ""

for stack in stacks:
    stack_tops += stack[0]

print(stack_tops)