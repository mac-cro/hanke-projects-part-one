# checks password strength
import sys

print("Please enter a good password!")
password = input()
print()

numbers = ['0','1','2','3','4','5t','6','7','8','9']

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

symbols = ['!','@','#','$','%','&','*']

invalid = [';','_','-','+','(',')']

x = 0

def password_run():
    def invalid_check(password):
        loop1 = 0
        yes = 0
        global x
        for x in range(len(invalid)):
            if invalid[loop1] in password:
                    yes += 1
            loop1 += 1
        
            if yes > 0:
            
                print("Your password contains invalid characters!")
                sys.exit()
                

    def num_check(password):
        loop1 = 0
        yes = 0
        global x
        for x in range(len(numbers)):
            if numbers[loop1] in password:
                    yes += 1
            loop1 += 1
        
        if yes > 0:
            print("Your password contains numbers.")
        else:
            print("Your password doesn't contain numbers!")

    def let_check(password):
        loop1 = 0
        yes = 0
        global x
        for x in range(len(letters)):
            if letters[loop1] in password:
                    yes += 1
            loop1 += 1
        
        if yes > 0:
            print("Your password contains letters.")
        else:
            print("Your password doesn't contain i!")

    def sym_check(password):
        loop1 = 0
        yes = 0
        global x
        for x in range(len(symbols)):
            if symbols[loop1] in password:
                    yes += 1
            loop1 += 1
        
        if yes > 0:
            print("Your password contains symbols.")
        else:
            print("Your password doesn't contain symbols!")

    def check_length(password):
        pass_length = len(password)

        if pass_length > 15:
            print("Your password is too long! (%s characters)"% pass_length)

        elif pass_length < 7:
            print("Your password is too short! (%s characters)"% pass_length)

        else:
            print("Your password is just the right length! (%s characters)"% pass_length)


    invalid_check(password)
    num_check(password)
    let_check(password)
    sym_check(password)
    check_length(password)    

password_run()
