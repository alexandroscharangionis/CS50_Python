import random

def main():
  level = get_level()
  generate_math_problems(level)

def get_level():
  while True:
    try:
      level = int(input('Level: '))
      if 0 < level <= 3:
        return level
    except ValueError:
      pass

def generate_integer(lvl):
  match lvl:
    case 1:
      return random.randint(0, 9)
    case 2:
      return random.randint(10, 99)
    case 3:
      return random.randint(100, 999)
    case _:
      raise ValueError


def evaluate_solution(int1, int2, r):
  return int1 + int2 == r

def generate_math_problems(lvl):
  correct_solutions = 0
  for i in range(0, 10):
    x = generate_integer(lvl)
    y = generate_integer(lvl)
    mistakes = 0
    for i in range(0, 3):
      try:
        solution = input(f'{x} + {y} = ')
        if evaluate_solution(x, y, int(solution)):
          correct_solutions += 1
          break
        elif not evaluate_solution(x, y, int(solution)):
          print('EEE')
          raise ValueError
      except ValueError:
        mistakes += 1
    if mistakes == 3:
      print(f'{x} + {y} = {x + y}')
  print(f'Score: {correct_solutions}')

if __name__ == "__main__":
  main()