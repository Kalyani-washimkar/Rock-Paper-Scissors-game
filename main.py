import random
print('WELCOME TO THE ROCK, PAPER, SCISSORS GAME!')
user_score = 0
computer_score = 0
options = ['rock', 'paper', 'scissors']
while True:
    user_input = input('Choose Rock or Paper or Scissors or q to quit: ').lower()
    if user_input == 'q':
        break
    computer_input = random.choice(options)
    print('computer takes', computer_input)
    if user_input == 'rock' and computer_input == 'paper':
        print('You lost.')
        computer_score += 1
    elif user_input == 'paper' and computer_input == 'scissors':
        print('Yo lost.')
        computer_score += 1
    elif user_input == 'scissors' and computer_input == 'rock':
        print('You lost.')
        computer_score += 1
    elif user_input == 'paper' and computer_input == 'rock':
        print('You won!!')
        user_score += 1
    elif user_input == 'scissors' and computer_input == 'paper':
        print('You won!!')
        user_score += 1
    elif user_input == 'rock' and computer_input == 'scissors':
        print('you won!!')
        user_score += 1
print('You won', user_score, 'times.')
print('Computer won', computer_score, 'times.')
print('Goodbye!')