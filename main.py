with open(file="input.txt", mode="r") as inputFile:
    with open(file="output.txt", mode="w") as outputFile:
        # input parsing
        line1, line2, line3, line4, line5 = inputFile.readlines()

        if (line1[:8] == "states=[" and line1[len(line1) - 2:-1]) == "]":
            states = line1[8: len(line1) - 2].split(',')
        else:
            outputFile.write("E0")
        if line2[:7] == "alpha=[" and line2[len(line2) - 2:-1] == "]":
            alpha = line2[7: len(line2) - 2].split(',')
        else:
            outputFile.write("E0")
        if line3[:9] == "initial=[" and line3[len(line3) - 2:-1] == "]":
            initial = line3[9: len(line3) - 2].split(',')
        else:
            outputFile.write("E0")
        if line4[:11] == "accepting=[" and line4[len(line4) - 2:-1] == "]":
            accepting = line4[11: len(line4) - 2].split(',')
        else:
            outputFile.write("E0")
        if line5[:7] == "trans=[" and line5[len(line5) - 2:-1] == "]":
            transitions = line5[7: len(line5) - 2].split(',')
        else:
            outputFile.write("E0")
print(states, alpha, initial, accepting, transitions)

# states=[on,off]
# alpha=[turn_on,turn_off]
# initial=[off]
# accepting=[]
# trans=[off>turn_on>off,on>turn_off>on]

# E0: Input file is malformed
# E1: A state 's' is not in the set of states
# E2: Some states are disjoint
# E3: A transition 'a' is not represented in the alphabet
# E4: Initial state is not defined
# E5: FSA is nondeterministic
