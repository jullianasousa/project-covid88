#2019-2020 Programação 2 (LTI)
#Grupo 23
#54950 Sofia Pedro Maciel Lourenço
#53927 Julliana dos Santos e Sousa

import sys
from SocialNetwork import SocialNetwork
from ContaminationList import ContaminationList
from ListOfPairs import ListOfPairs

inputFileName1, inputFileName2, outputFileName = sys.argv[1:]

# reads the contents of the file and creates class SocialNetwork
socialNetwork = SocialNetwork(inputFileName1)

# reads the contents of the file and creates class Pairs
pairs = ListOfPairs(inputFileName2, socialNetwork)

# checks for contamination between pairs and creates class Contamination List with the results
result = ContaminationList(pairs, socialNetwork)

# creates a file and write the results in it
fileOut = open(outputFileName, "w")
fileOut.write(str(result))
fileOut.close()