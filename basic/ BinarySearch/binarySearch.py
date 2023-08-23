from testData import test_data
import timeit

def binary_search(arr, n, l, r, val):
    while l <= r:
        mid = l + int(( r - l )/2)

        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            l = mid + 1
        else:
            r = mid - 1

    return -1

def launch(val, data):
    n = len(data)
    res = binary_search(data, n, 0, n-1, val)

    if res == -1:
        print(str(val) + ' Not found in the array')
    else:
        print(str(val) + ' Is in the ' + str(res) + ' position of the array')

val = 99999
data = test_data
iterations = 1

execution_time = timeit.timeit("launch(val, data)", globals=globals(), number=iterations)
average_time = execution_time / iterations
print(f"Average Time taken for {iterations} iteration: {average_time:.6f} seconds")