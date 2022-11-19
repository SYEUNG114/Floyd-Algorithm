import itertools

"""This is recursive version of Floyd's algorithm which is modified by the given example."""

def floyd(distance):
    
    MAX_LENGTH = len(distance)
    
    def recursive(start_node, end_node, intermediate):
        if intermediate == -1:
            return distance[start_node][end_node]

        else:
            return min(recursive(start_node, end_node, intermediate - 1),
                       recursive(start_node, intermediate, intermediate - 1) + recursive(intermediate, end_node,
                                                                                         intermediate - 1))
    for intermediate, start_node, end_node    in itertools.product    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        #return all possible paths and find the minimum
        distance[start_node][end_node] = recursive(start_node,end_node,intermediate)
    return distance
