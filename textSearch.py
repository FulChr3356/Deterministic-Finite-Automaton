'''/***************************************************************************
 * Name: Christopher Fulton
 * Email: CJFulton@email.sc.edu
 * Date/Time of Completion: TBD
 * 
 * Function:Text search  
 * 
 * Input: Text file containing string 
 * Output:The description of a DFA that accepts a string x if and only if w is a substring of x
 * 
 * Additional comments: 
 * 
 ###########################################################################/'''

import sys 
import math

def split(word): 
    return list(word) 

def subString(s,n): #Gets all possible substrings from given string 
    subS = []
    for i in range(n): 
        for len in range(i+1,n+1): 
            subS.append(s[i: len])
    return subS 
    

def construct(alphabet, word, subS):# Constructs general DFA from all posible substrings.For complete description all substring States have to still be indexed.
    i = 1
    k = 0
    dfa = {}
    j = 0
    letters = []
    for letter in word:
        letters.append(letter)

    for letter in letters:#Traverses string a sets next charecter as next state.
            if i == len(letters):
                break
            if letter == ' ' or letter =='\n':
                continue
            dfa.update({str(k): {letter:letters[i]}})
            i = i+1
            k = k + 1
    return dfa

### Driver Program
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
with open(sys.argv[1]) as f:
    lines = f. readlines()
word = lines[0]
subS =subString(word,len(word))
dfa = construct(alphabet,word,subS)
numStates = math.factorial(len(word))
print("Number of states: %s" % (numStates))
print("Accepting States: %s " % (subS))
word = split(word)
print("Alphabet: %s" % (str(word)))
print("DFA: %s" % (str(dfa)))