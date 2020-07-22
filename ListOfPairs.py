#2019-2020 Programação 2 (LTI)
#Grupo 23
#54950 Sofia Pedro Maciel Lourenço
#53927 Julliana dos Santos e Sousa

from SocialNetwork import SocialNetwork

class ListOfPairs:
    """
    Class of ListOfPairs
    """

    def __init__(self, fileName, socialNetwork):
        """
        Constructs a ListOfPairs

        Requires: fileName str and socialNetwork SocialNetwork
        """ 
        self._socialNetwork = socialNetwork
        self._pairs = self.setFromFile(fileName)
    
    def getSocialNetwork(self):
        """
        Gets the SocialNetwork
        """
        return self._socialNetwork

    def getListOfPairs(self):
        """
        Gets the a list with pairs
        """
        return self._pairs 
    
    def setListOfPairs(self, lst):
        """
        Set a new pairs list

        Requires: lst list
        Ensures: self.getPairs() == lst
        """
        self._pairs = lst
    
    def setSocialNetwork(self, newSocialNetwork):
        """
        Set a new SocialNetwork

        Requires: newSocialNetwork SocialNetwork
        Ensures: self.getSocialNetwork() == newSocialNetwork
        """
        self._socialNetwork = newSocialNetwork
    
    def setFromFile(self, fileName):
        """
        Reads a file and turns it into a list

        Requires: fileName str
        """

        fileIn = open(fileName, "r")
        pairsList = []

        for line in fileIn:
            elem1IsIn = False
            elem2IsIn = False
            temp = []
                                   
            line = line.strip().replace("\n", "").split(" ")

            # checks if the element is on the social network, 
            # if it is, the node equivalent to the name is added to a temporary list
            for elem in self.getSocialNetwork().getSocialNetworkList():
                if line[0] == elem.getName():
                    temp.append(elem)
                    elem1IsIn = True
            
            # checks if the element is on the social network 
            # if it is, the node equivalent to the name is added to a temporary list
            for elem in self.getSocialNetwork().getSocialNetworkList():
                if line[1] == elem.getName():
                    temp.append(elem)
                    elem2IsIn = True
            
            # add elements to the final list
            if elem1IsIn and elem2IsIn:             # if both elements are Node
                pairsList.append(temp)
            elif elem1IsIn:                         # if the first element of temp is Node and the second is a str
                pairsList.append([temp[0], line[1]])
            else:                                   # if the first element of temp is a str and the second is Node
                pairsList.append([line[0], temp[0]])
        
        return pairsList
    
    def __str__(self):
        """
        String representation of ListOfPairs
        """
        pairs = ""

        for elements in self.getListOfPairs():
            for e in elements:
                pairs += str(e) + " "
            pairs += "\n"
            
        return pairs

    def __lt__(self, other):
        """
        Verify if one pairs list is smaller than the other, if so,
        returns True, False otherwise.
        """
        return self._pairs < other._pairs
    
    def __eq__(self, other):
        """
        Verify if two list of pairs are equal.
        """
        return self._pairs == other._pairs