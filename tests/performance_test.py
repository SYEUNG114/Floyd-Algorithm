import test_case
import floyd_recursive
import floyd_imperative
import time

test = [test_case.test1, test_case.test2, test_case.test3, test_case.test4, test_case.test5, test_case.test6]

#Performance testing of recurstive Floyd’s algorithm
number = 1
print('Execution time using recursive function (in second):')
for i in test:
    
    start_time = time.perf_counter()
    floyd_recursive.floyd(i)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The execution time of test{number} is : {execution_time:.10f}s")
    number += 1

#Performance testing of imperative Floyd’s algorithm     
number = 1    
print('\nExecution time using imperative function (in second):')
for i in test:
    
    start_time = time.perf_counter()
    floyd_imperative.floyd(i)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The execution time of test{number} is : {execution_time:.10f}s")
    number += 1
