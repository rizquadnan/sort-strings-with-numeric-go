import time

from quick_sort import quick_sort
import number1m

start = time.time()
quick_sort(number1m.input_array, 0, len(number1m.input_array) - 1)
end = time.time()
elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')