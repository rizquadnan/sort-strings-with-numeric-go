import time

from selection_sort import selection_sort
import string1m

start = time.time()
selection_sort(string1m.input_array)
end = time.time()
elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')