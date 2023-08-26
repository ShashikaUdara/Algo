from testData import test_data
import timeit

def bubble_sort(data):
    for i in range(len(data) - 1):
        for j  in range(len(data) - 1 -i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

    return data

data = test_data
iterations = 1

execution_time = timeit.timeit("bubble_sort(data)", globals=globals(), number=iterations)
average_time = execution_time / iterations
print(f"Average Time taken for {iterations} iteration: {average_time:.6f} seconds")