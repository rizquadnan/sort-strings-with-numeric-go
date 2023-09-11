from string_number_conversion import alphabet_to_number

input_path="./dataset/1m.txt"
output_path="./string1m.py"

with open(input_path, 'r') as file:
  input_array = [line.strip() for line in file.readlines()]
  
# Write lines to a Python constant file
with open(output_path, 'w') as constant_file:
    constant_file.write(f'input_array = {input_array}\n')