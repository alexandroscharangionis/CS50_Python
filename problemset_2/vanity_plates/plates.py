def main():
  plate = input('Plate: ')

  if is_valid(plate):
    print('Valid')
  else:
    print('Invalid')

def is_valid(fullplate):
  if len(fullplate) < 2 or len(fullplate) > 6 or fullplate.isalnum() == False:
    return False
  else:
    return check_first_two_chars(fullplate) and check_first_number(fullplate) != False and check_last_chars(fullplate) != False

def check_first_two_chars(s):
  return s[0:2].isalpha()

def check_first_number(s):
  for i in range(len(s)):
    if s[i].isnumeric():
      if s[i] == '0':
        return False
      else:
        return True

def check_last_chars(s):
  for i in range(len(s)):
    if s[i].isdigit():
      if not s[i:].isdigit():
        return False
      else:
        return True
    else:
      continue

main()