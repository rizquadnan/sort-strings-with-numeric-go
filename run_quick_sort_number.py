import time
import sys

from quick_sort import quick_sort
import number1k
import number10k
import number100k
import number1m

if (len(sys.argv) != 2):
  raise Exception('Please provide 1 more args: 1k, 10k, 100k, or 1m')

if (sys.argv[1] == '1k'):
  input_array = number1k.input_array
elif (sys.argv[1] == '10k'):
  input_array = number10k.input_array
elif (sys.argv[1] == '100k'):
  input_array = number100k.input_array
elif (sys.argv[1] == '1m'):
  input_array = number1m.input_array


start = time.time()
quick_sort(input_array, 0, len(input_array) - 1)
end = time.time()
elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')