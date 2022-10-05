def main():
  plate = input('Plate: ')
  is_valid(plate)

def is_valid(s):
  if len(s) < 2 or len(s) > 6 or s.isalnum() == False or not s.isupper() or s == '':
    return False
  else:
    return check_first_two_chars(s) and check_first_number(s) != False and check_last_chars(s) != False

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

if __name__ == '__main__':
  main()