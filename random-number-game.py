import random

value = random.randint(1, 10)
tries = 0
guess = input('Guess a number between 1 to 10: ')
guess = int(guess)

while guess != value:
  if guess < value:
    print('Your guess is too low')
  elif guess > value:
    print('Your guess is too high')
  tries += 1
  guess = input('Try again: ')
  guess = int(guess)

  if tries == 2 and guess != value:
    print('Sorry, you lost. The right number is: ' + str(value))
    break

if guess == value:
  print('You guessed the right number: ' + str(value))

