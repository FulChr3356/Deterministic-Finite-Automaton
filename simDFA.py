'''/***************************************************************************
 * Name: Christopher Fulton
 * Email: CJFulton@email.sc.edu
 * Date/Time of Completion: TBD
 * 
 * Function: 
 * 
 * Input: Description of a DFA D from text file argument 1 and inout strings text file from argument 2
 * Output: Read any number of strings over D’s alphabet from another textfile, indicating (to standard output) whetherDaccepts or rejects eachof the strings.
 * 
 * Additional comments: 
 * 
 ###########################################################################/'''

import sys
# Constructs DFA using dictionaries to determine values of Alphabet
def construct(data):
    i = 0
    j = 0
    k = 0
    dfa = {}
    tempDFA = {}
    alphabet = []
    to_add = []
    letters = data[2].split("Alphabet: ")
    letters = letters[1].rstrip("\n")
    for letter in letters: #Create alphabet list
        alphabet.append(letter)
    for states in data: # Parses data from text file by delimiting values by  whitespace and newlines 
        if i > 2:
            states = states.split( )
            j = 0
            for state in states:
                if state == ' ' or state =='\n':
                    continue
                to_add.append({alphabet[j]:state}) # Temporary list for dictionary
                j = j+1
            for d in to_add:
                tempDFA.update(d) #Create temporay dictionary
            dfa.update({str(k):tempDFA}) #Add temp dict to DFA
            tempDFA = {}
            to_add = []
            k = k + 1
        i = i+1
    return dfa


def accepts(dfa,initial,accepting,string): #Traverses DFA, If state in accepting list, return true. 
    state = initial
    for charecter in string:
        state = dfa[state][charecter]
    return state in accepting


with open(sys.argv[1]) as f:
    lines = f. readlines()
with open(sys.argv[2]) as f2:
    asci = f2. readlines()
dfa = construct(lines)
i = 0
acceptStates = lines[1]
#Print results to standard output
st = acceptStates.split("Accepting states: ")
st = st[1].rstrip("\n")
st = st.split()
for x in asci:
    x = x.rstrip("\n")
    result = accepts(dfa,'0',st,x)
    if result == True:
        print("Accepts %s" % (x))
    if result == False:
        print("Rejects %s" % (x))
    







