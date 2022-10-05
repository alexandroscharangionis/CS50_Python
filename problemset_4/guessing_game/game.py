import random
import sys

def main():
  secret_number = generate_secret_number()
  guess_number(secret_number)

def generate_secret_number():
  while True:
    try:
      level = input('Level: ')
      n = random.randint(1, int(level))
    except ValueError:
      pass
    else:
      return n

def guess_number(secret_n):
  while True:
    try:
      guess = int(input('Guess: '))
      if guess < secret_n:
        print('Too small!')
      elif guess > secret_n:
        print('Too large!')
      else:
        print('Just right!')
        sys.exit()
    except ValueError:
      pass

main()