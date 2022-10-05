def main():
  expression = input ("Arithmetic expression: ")
  printResult(expression)

def printResult(exp):
  int1, operator, int2 = exp.split(" ")

  if operator == '+':
    result = int(int1) + int(int2)
    print (float(result))
  elif operator == '-':
    result = int(int1) - int(int2)
    print (float(result))
  elif operator == '*':
    result = int(int1) * int(int2)
    print (float(result))
  elif operator == '/':
    result = int(int1) / int(int2)
    print (float(result))

main()
