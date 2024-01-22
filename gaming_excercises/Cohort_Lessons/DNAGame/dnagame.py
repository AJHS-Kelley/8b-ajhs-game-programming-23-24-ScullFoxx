# DNA Replication Game, Sculley Alexandra, v1.2

# Import Entire Needed Modules -- Get the whole tool box.
import time, datetime

# Import Specific Methods -- Get the specific tool.
from random import choice

# Store the DNA Bases
i = 0
dnaBases = ["A", "T", "C", "G"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer number of bases to generate.\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1

    return dnaSequence



def doTranscription(dnaSequence: str, i: int) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence Uracil pairs with Adenine from the DNA sequence.\n")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan. 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence. Please leave no spaces! Then press enter.\n").upper()#.split()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    # while len(rnaSequence) > i:
    #     if rnaSequence[i] not in "AUGC":
    #         print(f"RNA {rnaSequence[i]} is wrong you lose")
    #         break
    #     else:
    #         i += 1
    #         continue
    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference items with the index.
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating.
    # Tuples CAN have duplicate values.



def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("Since the Sequences are not equal, they do not match.\n")
        return isMatch
    for dnaBase, rnaBase in zip (dnaSequence, rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "G":
            isMatch = True
        elif dnaBase == "G" and rnaBase == "C":
            isMatch = True
        elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
        else:
            print("They do not match because no base is True.\n")
    return isMatch

def calcScore(rnaSequence: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 3.0:
        score += 1000000
    elif rnaTime < 15.0:
        score += 5000
    else:
        score += 25000
        print("You tried your best.\n")

    scoreMulti = 0
    if len(rnaSequence)>= 10:
        scoreMulti = 3
    elif len(rnaSequence)>= 5:
        scoreMulti = 2
    else:
        scoreMulti = 1
    score *= scoreMulti
    return score

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime: float, score: float) ->  None:
    playerName = input("What is your first name?\n")
    lastName = input("What is your last name?\n")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore" + fullName + ".txt"
    saveData = open(fileName, "a")
    # File Modes
    # "x" mode -- Create file, if file exists, exit with error.
    # "w" mode -- Create file, if file exists, overwrite it.
    # "a" mode -- Creat file, if file exists, append it.
    saveData.write(f"DNA Sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time: {rnaTime}\n")
    saveData.write(f"Score: {score}\n")
    saveData.write(f"{fullName}\n")
    saveData.write(f"{datetime.datetime.now()}\n")
    saveData.close()

dna = genDNA()
rna = doTranscription(dna, i)
if verifySequence(dna, rna[0]):
    score = (calcScore(rna[0], rna[1]))
    saveScore(dna, rna[0], rna[1], score)