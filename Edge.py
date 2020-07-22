#2019-2020 Programação 2 (LTI)
#Grupo 23
#54950 Sofia Pedro Maciel Lourenço
#53927 Julliana dos Santos e Sousa

class Edge(object):
    """
    Class of Edges
    """

    def __init__(self, src, dest):
        """
        Constructs an Edge

        Requires: src and dst Nodes
        Ensures: src == self.getSource(), dest == self.getDestination(). 
        weight == dest.getFitness() * src.ageInverse()
        """ 
        self._src = src
        self._dest = dest
        self._weight = float(float(dest.getFitness()) * src.ageInverse())

    def getSource(self):
        """
        Gets the source of the edge
        """
        return self._src

    def getDestination(self):
        """
        Gets the destination of the edge
        """
        return self._dest
    
    def getWeight(self):
        """
        Gets the weight of the edge
        """
        return self._weight
    
    def setSource(self, source):
        """
        Set a new source

        Requires: source Node
        """
        self._src = source
    
    def setDestination(self, dest):
        """
        Set a new destination

        Requires: dest Node
        """
        self._dest = dest
    
    def setWeight(self, newWeight):
        """
        Set a new weight

        Requires: newWeight float
        """
        self._weight = newWeight

    def __str__(self):
        """
        String representation of Edge

        Ensures:
        String representation of Edge in format
        source Name -> dest Name
        """
        if type(self._src) == "str":
            return str(self._src) + '->' + self._dest.getName()
        elif type(self._dest) != "str":
            return self._src.getName() + '->' + str(self._dest)
        else:
            return str(self._src.getName()) + '->' + str(self._dest.getName())
    
    def __lt__(self, other):
        """
        Verify if one weight is smaller than the other, if so,
        returns True, False otherwise.
        """
        return self.getWeight() < other.getWeight()

    def __eq__(self, other):
        """
        Verify if one source is equal to another source and 
        one destination is equal to another destination.
        """
        return self.getSource() == other.getSource() and self.getDestination() == other.getDestination()