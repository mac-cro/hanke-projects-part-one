'''
WELCOME TO ROCK, PAPER, SCISSORS — SH00T!

created by mac_cro | 2.13.2020

Last Updated: 2.14.2020

V.1.8.5

'''

# enables random computer choice
import random

rounds = 0
player_points = 0
computer_points = 0

# greetings
print("\nWelcome to Rock, Paper, Scissors!")

# input name & display
player_name = input("Enter Name: ")
print("\nHello, %s!" % player_name)

# input rounds
rounds_num = int(input("Number of Rounds: "))

# choices for computer
choice_list = ['Rock', 'Paper', 'Scissors']

# runs loop per round
for x in range(rounds_num):

    # the game itself
    def play_game():
        global rounds
        print("Round: ", rounds + 1)
        rounds += 1

        # displays points
        print("\nPlayer: ", player_points, "| Computer: ", computer_points)
        
        # displays choices for player
        print("\nChoose Rock(1), Paper(2), or Scissors(3).")


        # if player chooses ROCK
        def rockChoice(player_choice, computer_choice):
            player_choice = 'rock'

            global rounds
            global player_points
            global computer_points

            if player_choice == 'rock' and computer_choice == 'scissors':
                print("Player wins round!")
                player_points += 1

                if rounds == rounds_num:
                    finish_game(player_points, computer_points)
                else:
                    play_game()
            

            elif player_choice == 'rock' and computer_choice == 'paper':
                print("Computer wins round!\n")
                computer_points += 1

                if rounds == rounds_num:
                    finish_game(player_points, computer_points)
                else:
                    play_game()
            

            elif player_choice == 'rock' and computer_choice == 'rock': 
                print("Tie!")

                if rounds == rounds_num:
                    finish_game(player_points, computer_points)
                else:
                    play_game()
            
        # if player chooses PAPER
        def paperChoice(player_choice, computer_choice):
            player_choice = 'paper'
            
            global rounds
            global player_points
            global computer_points

            if player_choice == 'paper' and computer_choice == 'scissors':
                print("Computer wins round!\n")
                
                player_points += 1
                if rounds == rounds_num:
                    finish_game(player_points, computer_points)
                else:
                    play_game()
            

            elif player_choice == 'paper' and computer_choice == 'rock':
                print("Player wins round!")
                computer_points += 1

                if rounds == rounds_num:
                    finish_game(player_points, computer_points)
                else:
                    play_game()
            
            
            elif player_choice == 'paper' and computer_choice == 'paper': 
                print("Tie!")
                
                if rounds == rounds_num:
                    finish_game(player_points, computer_points)
                else:
                    play_game()
            
        # if player chooses SCISSORS
        def scissorChoice(player_choice, computer_choice):
            player_choice = 'scissors'

            global rounds
            global player_points
            global computer_points

            if player_choice == 'scissors' and computer_choice == 'rock':
                print("Computer wins round!\n")
                player_points += 1

                if rounds == rounds_num:
                    finish_game(player_points, computer_points)
                else:
                    play_game()
            

            elif player_choice == 'scissors' and computer_choice == 'paper':
                print("Player wins round!")
                computer_points += 1

                if rounds == rounds_num:
                    finish_game(player_points, computer_points)
                else:
                    play_game()
            
            elif player_choice == 'scissors' and computer_choice == 'scissors': 
                print("Tie!")

                if rounds == rounds_num:
                    finish_game(player_points, computer_points)
                else:
                    play_game()
       
        # inputs & displays user choice
        player_choice = str(input())

        if player_choice == '1' or player_choice.lower() == 'rock':
            print("Player: Rock")
            player_choice = 'rock'

            # inputs & displays computer choice
            computer_choice = random.choice(choice_list)
            print("Computer: ", computer_choice)
            print()
            computer_choice = computer_choice.lower()

            rockChoice(player_choice, computer_choice)
            
        elif player_choice == '2' or player_choice.lower() == 'paper':
            print("Player: Paper")
            player_choice = 'paper'
            
            # inputs & displays computer choice
            computer_choice = random.choice(choice_list)
            print("Computer: ", computer_choice)
            print()
            computer_choice = computer_choice.lower()
            
            paperChoice(player_choice, computer_choice)
            
        elif player_choice == '3' or player_choice.lower() == 'scissors':
            print("Player: Scissors")
            player_choice = 'scissors'
            
            # inputs & displays computer choice
            computer_choice = random.choice(choice_list)
            print("Computer: ", computer_choice)
            print()
            computer_choice = computer_choice.lower()
            
            scissorChoice(player_choice, computer_choice)


    # if rounds meets max rounds, game finishes
    def finish_game(player_points, computer_points):

        print("Player: ", player_points)
        print("Computer: ", computer_points)
        print()

        if player_points > computer_points:
            print("Player %s won!" % player_name)

        elif player_points < computer_points:
            print("Player Computer won!")

        elif player_points == computer_points:
            print("It is a tie!")

        print("\nThanks for playing!\n")

    # checks number of rounds and continues OR ends game
    if rounds == rounds_num:
        finish_game(player_points, computer_points)
    else:
        play_game()