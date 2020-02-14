'''
P A S S W 0 R D . G E N E R A T O R !!!

created by mac_cro | 2.14.2020

'''

import random

characters = {
        
    'numbers' : ['0','1','2','3','4','5','6','7','8','9'],

    'letters' : ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I,''J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],

    'symbols' : ['!','@','#','$','%','&','*']

}

characters_symb = {
        
    'numbers' : ['0','1','2','3','4','5','6','7','8','9'],

    'letters' : ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I,''J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

}

characters_lett = {
        
    'numbers' : ['0','1','2','3','4','5','6','7','8','9'],

    'symbols' : ['!','@','#','$','%','&','*']

}

characters_numb = {

    'letters' : ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I,''J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],

    'symbols' : ['!','@','#','$','%','&','*']

}

print()

print("Welcome to the password generator!")

length = int(input('Input Length: '))

print('\nAnswer as Y or N:')
numb = input('Numbers? ').lower()
lett = input('Letters? ').lower()
symb = input('Symbols? ').lower()

def generate(numb, lett, symb):
    global length
    password = ''

    # all types
    if numb == 'y' and lett == 'y' and symb == 'y':
        for x in range(length):
            category = random.choice(list(characters.keys()))
            char = random.choice(characters.get(category))
            password += char

    # no numbers
    elif numb == 'n' and lett == 'y' and symb == 'y':
        for x in range(length):
            category = random.choice(list(characters_numb.keys()))
            char = random.choice(characters_numb.get(category))
            password += char
    # no letters
    elif numb == 'y' and lett == 'n' and symb == 'y':
        for x in range(length):
            category = random.choice(list(characters_lett.keys()))
            char = random.choice(characters_lett.get(category))
            password += char

    # no symbols
    elif numb == 'y' and lett == 'y' and symb == 'n':
        for x in range(length):
            category = random.choice(list(characters_symb.keys()))
            char = random.choice(characters_symb.get(category))
            password += char

    # only numbers
    elif numb == 'y' and lett == 'n' and symb == 'n':
        for x in range(length):
            char = random.choice(characters.get('numbers'))
            password += char
            
    # only letters
    elif numb == 'n' and lett == 'y' and symb == 'n':
        for x in range(length):
            char = random.choice(characters.get('letters'))
            password += char

    # only symbols
    elif numb == 'n' and lett == 'n' and symb == 'y':
        for x in range(length):
            char = random.choice(characters.get('symbols'))
            password += char

    else:
        print("Password: PASSW0RD")


    print()
    print("Your password is: ", password)
    print()


generate(numb, lett, symb)