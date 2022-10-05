from validator_collection import checkers

def main():
  print(validate_email(input('Email: ')))

def validate_email(mail):
  if checkers.is_email(mail):
    return 'Valid'
  else:
    return 'Invalid'

if __name__ == '__main__':
  main()
