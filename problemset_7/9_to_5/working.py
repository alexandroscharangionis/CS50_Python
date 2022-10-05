import re

def main():
  print(convert(input('Hours: ')))

def convert(s):
  s = s.strip()
  if matches := re.search(r"^((?:[1-9]|1[0-2])(?::(?:[0-5][0-9]))? (?:AM|PM)) to ((?:[1-9]|1[0-2])(?::(?:[0-5][0-9]))? (?:AM|PM))$", s):
    group1 = format(matches.group(1))
    group2 = format(matches.group(2))
    return f'{group1} to {group2}'
  else:
    raise ValueError('Wrong input')

def format(match):
  if 'AM' in match and ':' in match:
    time, meridian = match.split(' ')
    hrs, min = time.split(':')
    if int(hrs) < 10:
      return f'{int(hrs):02}:{min}'
    elif int(hrs) > 10 and int(hrs) != 12:
      return f'{int(hrs)}:{min}'
    else:
      return f'00:{min}'
  elif 'PM' in match and ':' in match:
    time, meridian = match.split(' ')
    hrs, min = time.split(':')
    if int(hrs) != 12:
      return f'{int(hrs) + 12}:{min}'
    else:
      return f'12:{min}'
  elif 'AM' in match and not ':' in match:
    hrs, meridian = match.split(' ')
    if int(hrs) < 10:
      return f'{int(hrs):02}:00'
    elif int(hrs) > 10 and int(hrs) != 12:
      return f'{int(hrs)}:00'
    else:
      return f'00:00'
  else:
    hrs, meridian = match.split(' ')
    if int(hrs) != 12:
      return f'{int(hrs) + 12}:00'
    else:
      return f'12:00'

if __name__ == '__main__':
  main()