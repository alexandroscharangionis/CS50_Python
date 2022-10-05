
def main():
  while True:
    try:
      fraction = input('Insert fraction: ')
      integer = convert(fraction)
      print(gauge(integer))
      break
    except ValueError:
      print('Please use integers only.\nAlso, make sure numerator is smaller than denominator.')
    except ZeroDivisionError:
      print('Can\'t divide by zero.')

def convert(fraction):
  x, y = fraction.split('/')
  if int(x) > int(y) and int(y) != 0:
    raise ValueError
  result = round(int(x) / int(y) * 100)
  return result

def gauge(percentage):
  if percentage <= 1:
    return 'E'
  elif percentage >= 99:
    return 'F'
  else:
    return f'{percentage}%'

if __name__ == '__main__':
  main()