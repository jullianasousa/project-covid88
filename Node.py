#2019-2020 Programação 2 (LTI)
#Grupo 23
#54950 Sofia Pedro Maciel Lourenço
#53927 Julliana dos Santos e Sousa

class Node:
    """
    Class of Node
    """

    def __init__(self, name, idNb, age, direct, fitness, immune):
        """
        Constructs a Node

        Requires: name, idNb, age, direct, fitness, immune str
        Ensures: name == self.getName(), idNb == self.getID(), age == self.getAge(),
        direct == self.getDirect(), fitness == self.getFitness(), immune == self.getImmunity()
        """ 
        self._name = name
        self._id = idNb
        self._age = age
        self._direct = direct
        self._fitness = fitness
        self._immune = immune
    
    def getName(self):
        """
        Name of node

        Ensures:
        Name of node
        """
        return self._name
    
    def getID(self):
        """
        ID of node

        Ensures:
        ID of node
        """
        return self._id
    
    def getAge(self):
        """
        Age of node

        Ensures: Age of node
        """
        return self._age
    
    def getDirect(self):
        """
        Direction of node

        Ensures: Direct of node
        """
        return self._direct
    
    def getFitness(self):
        """
        Fitness of node

        Ensures: Fitness of node
        """
        return self._fitness
    
    def getImmunity(self):
        """
        Immune of node

        Ensures: Immune of node
        """
        return self._immune
    
    def setName(self, name):
        """
        Set a new name

        Requires: name str
        """
        self._name = name
    
    def setID(self, idNb):
        """
        Set a new ID

        Requires: idNb str
        """
        self._id = idNb
    
    def setAge(self, age):
        """
        Set a new age

        Requires: age str
        """
        self._age = age
    
    def setDirect(self, direct):
        """
        Set a new direct

        Requires: direct str
        """
        self._direct = direct
    
    def setFitness(self, fitness):
        """
        Set a new fitness

        Requires: fitness str
        """
        self._fitness = fitness
    
    def setImmunity(self, immune):
        """
        Set a new immunity

        Requires: immune str
        """
        self._immune = immune
    
    def ageInverse(self):
        """
        Inverse of age of a given item
        """
        return 1.0/int(self.getAge())
        
    def __str__(self):
        """
        String representation of node

        Ensures:
        String representation of Node in format
        <name, idNb, age, direct, fitness, immune>
        """
        
        result = '<' + self._name + ', ' + str(self._id) + ', ' + self._age + ', ' 
        for elem in self._direct:
            result += elem.getID() + ', '
        result += self._fitness + ', ' + self._immune + '>'

        return result
    
    def __eq__(self, other):
        """
        Verify if two names are equal.
        """
        return self.getName() == other.getName()

    def __lt__(self, other):
        """
        Verify if one age is smaller than the other, if so,
        returns True, False otherwise.
        """
        return self.getAge() < other.getAge()