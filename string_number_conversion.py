def alphabet_to_number(string):
    string = string.upper()
    result = 0
    for char in string:
        if 'A' <= char <= 'Z':
            result = result * 27 + (ord(char) - ord('A') + 1)
        else:
            # input @ padding case
            if char == '@':
                result = result * 27 + 27
            pass
    return result

def number_to_alphabet(number):
    result = ""
    
    while number > 0:
        remainder = (number - 1) % 27 
        if remainder == 26:  # Handle the special case for @ padding
            result = '@' + result
        else:
            result = chr(remainder + ord('A')) + result  
        number = (number - remainder - 1) // 27 
    
    return result