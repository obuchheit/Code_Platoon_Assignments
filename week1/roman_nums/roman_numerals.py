def to_roman(n):
    roman_to_integer = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
    }
    output = ''
    cnum = 0

    for (key, value) in roman_to_integer.items():
        if n >= value:
            cnum = (n - (n % value)) / value
            output += (key * int(cnum))
            n = n % value
            
    return output




