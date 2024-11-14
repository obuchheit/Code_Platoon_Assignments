def caesar_cipher(string, shift_amount):
    alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    lowString = string.lower()
    answer = ''

    for index, l in enumerate(lowString):
        if l in alph_list:
            new_index = index + shift_amount
            if new_index > 25:
                new_index -= 25
                
            answer += alph_list[new_index]
        else:
            answer += l
            
        print(answer)

caesar_cipher("Hello zach168! Yes here.", 5)