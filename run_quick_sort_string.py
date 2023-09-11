import time

from quick_sort import quick_sort
import string1m

start = time.time()
quick_sort(string1m.input_array, 0, len(string1m.input_array) - 1)
end = time.time()
elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')