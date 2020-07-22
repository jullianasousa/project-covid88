#2019-2020 Programação 2 (LTI)
#Grupo 23
#54950 Sofia Pedro Maciel Lourenço
#53927 Julliana dos Santos e Sousa

from Node import Node

class SocialNetwork:
    """
    Class of SocialNetwork
    """

    def __init__(self, fileName):
        """
        Constructs a SocialNetwork

        Requires: fileName str
        """ 
        self._socialNetwork = self.setFromFile(fileName)
    
    def getSocialNetworkList(self):
        """
        Gets the SocialNetworkList
        """
        return self._socialNetwork
    
    def setSocialNetworkList(self, newSocialNetwork):
        """
        Set a new SocialNetworkList

        Requires: newSocialNetwork list
        Ensures: self.getSocialNetworkList() == newSocialNetwork
        """
        self._socialNetwork = newSocialNetwork
    
    def setFromFile(self, fileName):
        """
        Reads a file and turns it into a list

        Requires: fileName str
        """
        
        fileIn = open(fileName, "r")
        socialNetwork = []

        fileIn.readline()
        for line in fileIn:
            connections = []                                             
            line = line.strip().replace("\n", "").replace("<", "").replace(">", "").split(", ")
            lineLen = len(line)

            for i in range(3, (lineLen - 2)):
                connections.append(line[i])

            socialNetwork.append(Node(line[0], line[1], line[2], connections, line[lineLen-2], line[lineLen - 1]))
        
        # changes the elements of the Direct attribute to Node
        for item in socialNetwork:
            temp = []
            for directItem in item.getDirect():
                for elem in socialNetwork:
                    if directItem == elem.getID():
                        temp.append(elem)
            item.setDirect(temp)


        fileIn.close()

        return socialNetwork
    
    def __str__(self):
        """
        String representation of SocialNetwork
        """
        network = ""

        for elem in self._socialNetwork:
            network += '<' + elem._name._name + ', ' + str(elem._name._id) + ', ' + elem._name._age + ', ' 
            for i in elem._name._direct:
                network += str(i) + ', '
            network += elem._name._fitness + ', ' + elem._name._immune + '>' + "\n"

        return network
    
    def __lt__(self, other):
        """
        Verify if one social network is smaller than the other, if so,
        returns True, False otherwise.
        """
        return self._socialNetwork < other._socialNetwork

    def __eq__(self, other):
        """
        Verify if two social network lists are equal.
        """
        return self._socialNetwork == self._socialNetwork
