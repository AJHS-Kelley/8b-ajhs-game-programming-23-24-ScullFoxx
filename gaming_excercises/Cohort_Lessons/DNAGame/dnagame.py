# DNA Replication Game, Sculley Alexandra, v0.2

# Import Entire Needed Modules -- Get the whole tool box.
import time, datetime

# Import Specific Methods -- Get the specific tool.
from random import choice

# Store the DNA Bases
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



def genRNA(dnaSequence: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence Uracil pairs with Adenine from the DNA sequence.\n")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan. 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart


    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference items with the index.
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating.
    # Tuples CAN have duplicate values.

dna = genDNA()
rna = genRNA(dna)
print(rna)