# Linear Search

from testData import test_data
import timeit

def linear_search(val, data):
    for i in range(len(data)):
        if val == data[i]:
            return i

# 29070 is the last data element of the data set
val = 29070
data = test_data
iterations = 1

execution_time = timeit.timeit("linear_search(val, data)", globals=globals(), number=iterations)
average_time = execution_time / iterations
print(f"Average Time taken for {iterations} iteration: {average_time:.6f} seconds")