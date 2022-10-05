import sys

def main():
  print(count_lines())

def count_lines():
  if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
  elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
  elif not sys.argv[1].endswith('.py'):
    sys.exit('Not a Python file')
  else:
    try:
      total_lines = 0
      with open(sys.argv[1]) as file:
        for line in file:
          if line.strip().startswith('#') or line.isspace():
            continue
          else:
            total_lines += 1
      return total_lines
    except FileNotFoundError:
      sys.exit('File does not exist')

if __name__ == '__main__':
  main()