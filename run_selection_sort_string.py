import time
import sys

from selection_sort import selection_sort
import string1k
import string10k
import string100k
import string1m

if (len(sys.argv) != 2):
  raise Exception('Please provide 1 more args: 1k, 10k, 100k, or 1m')

if (sys.argv[1] == '1k'):
  input_array = string1k.input_array
elif (sys.argv[1] == '10k'):
  input_array = string10k.input_array
elif (sys.argv[1] == '100k'):
  input_array = string100k.input_array
elif (sys.argv[1] == '1m'):
  input_array = string1m.input_array

start = time.time()
selection_sort(input_array)
end = time.time()
elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')