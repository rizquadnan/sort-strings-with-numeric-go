def alphabet_to_number(string):
    string = string.upper()  # Convert to uppercase for consistency
    result = 0
    for char in string:
        if 'A' <= char <= 'Z':
            result = result * 27 + (ord(char) - ord('A') + 1)
        else:
            # Handle non-alphabetic characters if needed
            if char == '@':
                result = result * 27 + 27
            pass
    return result

def number_to_alphabet(number):
    result = ""
    
    while number > 0:
        remainder = (number - 1) % 27  # Get the remainder
        if remainder == 26:  # Handle the special case for '@'
            result = '@' + result
        else:
            result = chr(remainder + ord('A')) + result  # Convert back to character and add to result
        number = (number - remainder - 1) // 27  # Update the number
    
    return result
    
string_num = "HELLZ@"
result = alphabet_to_number(string_num)