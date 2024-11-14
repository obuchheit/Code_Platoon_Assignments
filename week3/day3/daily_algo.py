'''
Create a function called encode() to replace all the lowercase vowels in a given string with numbers accourdingly to the following pattern.
a = 1
e = 2
i = 3
o = 4
u = 5

for example encode("hello") would return "h2ll4
create a function calles decode() that turns them back
'''
vows = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}

def encode(str):
    encoded_str = ''
    for l in str:
        if l in vows:
            encoded_str += vows[l] 
        else:
            encoded_str += l
    return encoded_str


def decode(str):
    decoded_str = ''

    for l in str:
        if l.isnumeric():
                decoded_str += list(vows.keys())[int(l)-1]
        else:
            decoded_str += l
    return decoded_str

print(decode("h2ll4"))