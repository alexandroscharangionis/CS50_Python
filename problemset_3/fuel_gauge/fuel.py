def main():
  while True:
    try:
      fraction = input('Insert fraction: ')
      get_fuel_level(fraction)
      break
    except ValueError:
      print('Please use integers only.\nAlso, make sure numerator is smaller than denominator.')
    except ZeroDivisionError:
      print('Can\'t divide by zero.')


def get_fuel_level(f):
  x, y = f.split('/')
  if int(x) > int(y):
    x = 'cat'
  result = round( int(x) / int(y) * 100)
  if result <= 1:
    print('E')
  elif result >= 99:
    print('F')
  else:
    print(f'{result}%')

main()