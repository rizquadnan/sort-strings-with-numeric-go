import time

from selection_sort import selection_sort
import number100k

start = time.time()
res = selection_sort(number100k.input_array)
end = time.time()
elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')
