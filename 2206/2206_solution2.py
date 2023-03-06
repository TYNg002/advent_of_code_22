with open("2206_input.txt") as inputfile:
    input = inputfile.read()

# store characters to be assessed
assess = []

for num, char in enumerate(input, 1):
    if num < 14:
        assess.append(char)
    else:
        assess.append(char)
        repeat = False
        for item in assess:
            # count occurrences of item in assess
            counter = 0
            for item2 in assess:
                if item == item2:
                    counter += 1
                # if counter is greater than 1, it means a repeat exists
                if counter > 1:
                    repeat = True
                    break
            # exit loop if repeat is detected
            if repeat == True:
                break
        # if all items have been iterated through and no repeat exists in assess
        if repeat == False:
            print(num)
            exit()
        assess.pop(0)