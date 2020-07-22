#2019-2020 Programação 2 (LTI)
#Grupo 23
#54950 Sofia Pedro Maciel Lourenço
#53927 Julliana dos Santos e Sousa

from SocialNetwork import SocialNetwork
from Graph import Graph
from Edge import Edge

class ContaminationList:
    """
    Class of ContaminationList
    """

    def __init__(self, pairs, socialNetwork):
        """
        Constructs a ContaminationList

        Requires: pairs ListOfPairs and socialNetwork SocialNetwork
        """ 
        self._socialNetwork = socialNetwork
        self._listOfPairs = pairs
        self._contaminationList = self.checkContamination()

    def getSocialNetwork(self):
        """
        Gets the SocialNetwork
        """
        return self._socialNetwork

    def getPairs(self):
        """
        Gets the ListOfPairs
        """
        return self._listOfPairs 
    
    def getContaminationList(self):
        """
        Gets the ContaminationList list
        """
        return self._contaminationList
    
    def setPairs(self, lst):
        """
        Set a new ListOfPairs

        Requires: lst ListOfPairs
        Ensures: self.getPairs() == lst
        """
        self._listOfPairs = lst
    
    def setSocialNetwork(self, newSocialNetwork):
        """
        Set a new SocialNetwork

        Requires: newSocialNetwork SocialNetwork
        Ensures: self.getSocialNetwork() == newSocialNetwork
        """
        self._socialNetwork = newSocialNetwork
    
    def setContaminationList(self, lst):
        """
        Set a new ContaminationList list
        
        Requires: lst ContaminationList
        Ensures: self.getContaminationList() == lst
        """
        self._contaminationList = lst
    
    def items(self):
        """
        Supports iteration over the current instance
        """
        for elem in self.getSocialNetwork().getSocialNetworkList():
            yield elem

    def createNodes(self, graph):
        """
        Create nodes in graph
        Requires: graph Graph
        """
        for elem in self.items():
            graph.addNode(elem)
    
    def createEdges(self, graph):
        """
        Create edges in graph
        Requires: graph Graph
        """
        for elem in self.items():
            for e in elem.getDirect():
                graph.addEdge(Edge(elem, e))
    
    def checkContamination(self):
        """
        Checks for contamination between pairs

        Ensures: List the elements are the results obtained 
        when comparing the elements of the ListOfPairs class.
        If one of the elements is a string, add it as "out of the social network", 
        if not a string, check if there is contamination between 
        them and how long it will take for the contamination to occur
        """
        g = Graph()
        fileOut = []

        # create nodes and edges
        self.createNodes(g)
        self.createEdges(g)
        
        # scrolls through the list of pairs. if one of the elements is a string, 
        # add it as "out of the social network", 
        # if not a string, check if there is contamination between them 
        # and how long it will take for the contamination to occur
        for elem in self.getPairs().getListOfPairs():
            if type(elem[0]) != str and type(elem[1]) != str:
                sp = self.search(g, elem[0], elem[1]) # search for the lighter path from elem[0] to elem[1]
                if sp != None:
                    print('Lighter path found by DFS:', self.printPath(sp))
                    contaminationTime = round(self.sumWeight(g, sp) * 24)
                    fileOut.append(str(contaminationTime))
                else:
                    fileOut.append("No contagion between " + elem[0].getName() + " and " + elem[1].getName())
            elif type(elem[0]) != str: # checks if elem[1] is out of the social network
                fileOut.append(elem[1] + " out of the social network")
            else: # checks if elem[0] is out of the social network
                fileOut.append(elem[0] + " out of the social network")
            

        return fileOut
            

    def printPath(self, path):
        """
        Print the path

        Requires: path a list of nodes
        """
        result = ''
        for i in range(len(path)):
            result = result + str(path[i].getName())
            if i != len(path) - 1:
                result = result + '->'
        return result
    

    def sumWeight(self, graph, lst):
        """
        Sum of the weights of a list

        Requires: graph Graph, lst list
        Ensures: Sum of the weights of a list
        """
        acc = 0
        if lst != None: # checks if the list is empty
            for i in range(len(lst) - 1):
                for node, weight in graph.childrenOf(lst[i]):
                    if node == lst[i+1]: # checks if the next element of lst is one of the children of lst[i], if so, it adds its weight to the accumulator
                        acc += weight
        return acc
    

    def verifyImmunity(self, lst):
        """
        Checks if all elements of a list are not immune to the virus

        Requires: lst list
        Ensures: True if all elements of a list are not immune to the virus, 
        False otherwise.
        """
        for elem in lst:
            if elem.getImmunity() == "Yes":
                return False
        return True

    def DFS(self, graph, start, end, path, lighter):
        """
        The lighter path from start to end in graph

        Requires:
        graph a Graph;
        start and end nodes;
        path and lighter lists of nodes
        Ensures:
        the lighter path from start to end in graph
        """
        path = path + [start]
        print('Current DFS path:', self.printPath(path))

        if start == end:
            return path
        for node, weight in graph.childrenOf(start):
            if node not in path:
                if (lighter == None or self.sumWeight(graph, path) < self.sumWeight(graph, lighter)) and self.verifyImmunity(path) == True:
                    newPath = self.DFS(graph, node, end, path, lighter)
                    if newPath != None and self.verifyImmunity(newPath) == True and (lighter == None or self.sumWeight(graph, newPath) < self.sumWeight(graph, lighter)):
                        lighter = newPath
        return lighter
    

    def search(self, graph, start, end):
        """
        Lighter path from start to end in graph

        Requires:
        graph a Digraph;
        start and end are nodes
        Ensures:
        lighter path from start to end in graph
        """
        return self.DFS(graph, start, end, [], None)


    def __str__(self):
        """
        String representation of ContaminationList
        """
        lst = ""
        lenList = len(self.getContaminationList())
        cont = 1

        for elem in self.getContaminationList():
            if cont != lenList:
                lst += str(elem) + "\n"
            else:
                lst += str(elem)
            cont += 1
        
        return lst
    
    def __lt__(self, other):
        """
        Verify if one contamination list is smaller than the other, if so,
        returns True, False otherwise.
        """
        return self._contaminationList < other._contaminationList

    def __eq__(self, other):
        """
        Verify if two contamination lists are equal.
        """
        return self._contaminationList == other._contaminationList
