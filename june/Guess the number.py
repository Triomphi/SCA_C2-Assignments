import random

def computer():
    num = random.randint(1, 20)
    print('Hey there!, I am thinking of a number between 1 and 20.')
    return num

def game(number):
    guesses = 0

    while guesses < 3:
        print('Take a guess.') 
        guess = int(input())
        guesses = guesses + 1

        if guess < number:
            print('Your guess is too low.') 
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            break

    if guess == number:
        print('Good job,! You guessed my number in ' + str(guesses) + ' guesses!')
    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

playAgain = "yes"
while playAgain == "yes":
    guessed_number = computer()
    game(guessed_number)

    print("Do you want to play again? (yes or no)")
    playAgain = input()
    if playAgain == 'no':
        print('Bye!')
    










        
          
    
