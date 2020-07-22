#2019-2020 Programação 2 (LTI)
#Grupo 23
#54950 Sofia Pedro Maciel Lourenço
#53927 Julliana dos Santos e Sousa

class Digraph(object):
    """
    Class of Digraph
    """
    
    def __init__(self):
        """
        Constructs a Digraph

        Ensures: nodes is a list of the nodes in the graph
        edges is a dict mapping each node to a list of its children
        """ 
        self._nodes = []
        self._edges = {}
    
    def getNodes(self):
        """
        Gets list of nodes
        """
        return self._nodes
    
    def getEdges(self):
        """
        Gets edges
        """
        return self._edges
    
    def setNodes(self, nodes):
        """
        Set a new list of nodes

        Requires: nodes list
        Ensures: self.getNodes() == nodes
        """
        self._nodes = nodes

    def setEdges(self, edges):
        """
        Set a new dict of edges

        Requires: edges dict
        Ensures: self.getEdges() == edges
        """
        self._edges = edges

    def addNode(self, node):
        """
        Adds a node to the graph

        Requires: node Node
        Ensures: if node is not in the node list, adds a new node 
        to the nodes list and creates an item for the edge dict 
        with an empty list as value and the ID of the new node as the key
        """
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node.getID()] = []

    def addEdge(self, edge):
        """
        Adds an edge to the graph

        Requires: edge Edge
        Ensures: edge[src.getID()] = (dest, weight)
        """
        src = edge.getSource()
        dest = edge.getDestination()
        weight = edge.getWeight()
        if not(src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        if (dest, weight) not in self._edges[src.getID()]:
            self._edges[src.getID()].append((dest, weight))

    def childrenOf(self, node):
        """
        Returns the children of a node

        Requires: node Node
        Ensures: returns the value of edge dict that has
        node.getID() as a key
        """
        return self._edges[node.getID()]

    def hasNode(self, node):
        """
        Checks if the node already exists in the node list

        Requires: node Node
        Ensures: True if node is already in the node list, False otherwise
        """
        return node in self._nodes

    def __str__(self):
        """
        String representation of Digraph

        Ensures:
        String representation of Digraph in format
        sourceName -> destinationName
        """
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src.getName() + '->'\
                + dest.getName() + '\n'
        return result
    
    def __lt__(self, other):
        """
        Verify if one nodes list is smaller than the other, if so,
        returns True, False otherwise.
        """
        return self._nodes < other._nodes

    def __eq__(self, other):
        """
        Verify if two list of nodes are equal.
        """
        return self._nodes == other._nodes