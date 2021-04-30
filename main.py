with open(file="input.txt", mode="r") as inputFile:
    with open(file="output.txt", mode="w") as outputFile:

        line1, line2, line3, line4, line5 = inputFile.readlines()
        eLine1 = line1[:8] == "states=[" and line1[len(line1) - 2:-1] == "]"
        eLine2 = line2[:7] == "alpha=[" and line2[len(line2) - 2:-1] == "]"
        eLine3 = line3[:9] == "initial=[" and line3[len(line3) - 2:-1] == "]"
        eLine4 = line4[:11] == "accepting=[" and line4[len(line4) - 2:-1] == "]"
        eLine5 = line5[:7] == "trans=[" and line5[len(line5) - 2:-1] == "]"

        # Error0 handling
        if not eLine1 or not eLine2 or not eLine3 or not eLine4 or not eLine5:
            outputFile.write("Error:\nE0: Input file is malformed")
            exit()

        # input parsing
        states = line1[8: len(line1) - 2].split(',')
        alphabet = line2[7: len(line2) - 2].split(',')
        initial = line3[9: len(line3) - 2].split(',')
        accepting = line4[11: len(line4) - 2].split(',')
        transitions = line5[7: len(line5) - 2].split(',')

        # print(states, alphabet, initial, accepting, transitions)

        dic = {}
        # Error2 handling
        for transit in states:
            dic[transit] = 0
        for transit in transitions:
            state1 = transit[:transit.find(">")]
            state2 = transit[transit.rfind(">") + 1:]
            if state1 != state2:
                if state1 in dic.keys():
                    dic[state1] = 1

                if state2 in dic.keys():
                    dic[state2] = 1

        for _, value in dic.items():
            if value == 0:
                outputFile.write("Error:\nE2: Some states are disjoint")
                exit()

        # Error1 handling
        if initial[0] not in states:
            outputFile.write("Error:\nE1: A state 's' is not in the set of states")
            exit()
        for state in accepting:
            if state not in states and len(state) > 0:
                outputFile.write("Error:\nE1: A state '" + state + "' is not in the set of states")
                exit()
        for transit in transitions:
            state1 = transit[:transit.find(">")]
            state2 = transit[transit.rfind(">") + 1:]
            if state1 not in states and len(state1) > 0:
                outputFile.write("Error:\nE1: A state '" + state1 + "' is not in the set of states")
                exit()
            if state2 not in states and len(state2) > 0:
                outputFile.write("Error:\nE1: A state '" + state2 + "' is not in the set of states")
                exit()

        # Error3 handling
        for transit in transitions:
            probableTransition = transit[transit.find(">") + 1:transit.rfind(">")]
            if probableTransition not in alphabet:
                outputFile.write("Error:\nE3: A transition 'a' is not represented in the alphabet")
                exit()

        # Error4 handling
        if len(initial) == 0:
            outputFile.write("Error:\nE4: Initial state is not defined")
            exit()

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
