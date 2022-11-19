"""
This file contains 6 test cases and the expected outputs are generated by the imperative function.
"""

import sys
NO_PATH = sys.maxsize

# Test 1: Graph with 4 nodes (provided in example)
test1 = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

output1 = [[0, 7, 12, 8],
        [9223372036854775807, 0, 5, 7],
        [9223372036854775807, 9223372036854775807, 0, 2],
        [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]

# Test 2: Graph with 4 nodes (distances between nodes are self-defined)
test2 = [[0, 5, NO_PATH, 9],
         [4, 0, 8, NO_PATH],
         [NO_PATH, 3, 0, 5],
         [NO_PATH, 6, NO_PATH, 0]]

output2 = [[0, 5, 13, 9], 
             [4, 0, 8, 13], 
             [7, 3, 0, 5], 
             [10, 6, 14, 0]]

# Test 3: Graph with 3 nodes (distances between nodes are self-defined)
test3 = [[0, NO_PATH, 9],
         [NO_PATH, 0, NO_PATH],
         [NO_PATH, 3, 0]]

output3 = [[0, 12, 9],
             [9223372036854775807, 0, 9223372036854775807],
             [9223372036854775807, 3, 0]]


# Test 4: Graph with 6 nodes (distances between nodes are self-defined)
test4 = [[0, 7, NO_PATH, 5, NO_PATH, NO_PATH],
         [NO_PATH, 0, 2, NO_PATH, 9, NO_PATH],
         [3, NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH],
         [2, NO_PATH, NO_PATH, 0, NO_PATH, 3],
         [NO_PATH, 3, 6, NO_PATH, 0, NO_PATH],
         [NO_PATH, NO_PATH, 2, NO_PATH, NO_PATH, 0]]

output4 = [[0, 7, 9, 5, 16, 8],
             [5, 0, 2, 10, 9, 13],
             [3, 10, 0, 8, 19, 11],
             [2, 9, 5, 0, 18, 3],
             [8, 3, 5, 13, 0, 16],
             [5, 12, 2, 10, 21, 0]]


# Test 5: Graph with 1 node
test5 = [[0]]

output5 = [[0]]


# Test 6: Graph with negative paths (distances between nodes are-self defined)
test6 = [[0, -7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, -2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

output6 = [[0, -7, -2, -4],
             [9223372036854775807, 0, 5, 3],
             [9223372036854775805, 9223372036854775798, 0, -2],
             [9223372036854775807, 9223372036854775800, 9223372036854775805, 0]]
