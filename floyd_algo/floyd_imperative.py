import itertools

"""This is imperative version of Floyd's algorithm given by the assignment"""

def floyd(distance):
    MAX_LENGTH = len(distance)
    for intermediate, start_node,end_node    in itertools.product    (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        #return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node] )
    return distance
