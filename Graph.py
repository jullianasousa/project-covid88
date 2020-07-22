#2019-2020 Programação 2 (LTI)
#Grupo 23
#54950 Sofia Pedro Maciel Lourenço
#53927 Julliana dos Santos e Sousa

from Digraph import Digraph
from Edge import Edge

class Graph(Digraph):
    """
    Class of Graph. Subclass of Digraph
    """
    
    def addEdge(self, edge):
        """
        Adds an edge to the graph

        Requires: edge Edge
        Ensures: edge[src] = dest and edge[dest] = src 
        """
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
    
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
        Verify if one edge dict is smaller than the other, if so,
        returns True, False otherwise.
        """
        return self._edges < other._edges

    def __eq__(self, other):
        """
        Verify if two edges dict are equal.
        """
        return self._edges == other._edges