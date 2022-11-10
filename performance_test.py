
import test_case
import floyd_recursive
import floyd_imperative
import time

#Performance testing of recurstive Floyd’s algorithm 

test = [test_case.test1, test_case.test2, test_case.test3, test_case.test4, test_case.test5, test_case.test6]
number = 1
print('Recursive method:')
for i in test:
    
    start_time = time.perf_counter()
    floyd_recursive.floyd(i)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The execution time of test{number} is : {execution_time:.10f}s")
    number += 1

#Performance testing of imperative Floyd’s algorithm 

test = [test_case.test1, test_case.test2, test_case.test3, test_case.test4, test_case.test5, test_case.test6]
number = 1
print('Imperative method:')
for i in test:
    
    start_time = time.perf_counter()
    floyd_imperative.floyd(i)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The execution time of test{number} is : {execution_time:.10f}s")
    number += 1
