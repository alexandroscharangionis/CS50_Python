def main():
  greeting = input("Type a greeting ").strip().lower()
  evalGreeting(greeting)

def evalGreeting(str):
  if str.startswith('hello'):
    print('$0')
  elif str.startswith('h'):
    print('$20')
  else:
    print ('$100')

main()