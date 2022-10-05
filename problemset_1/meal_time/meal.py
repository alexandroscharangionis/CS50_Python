def main():
  time = input("What time is it? ")
  if 7 <= convert(time) <= 8:
    print('breakfast time')
  elif 12 <= convert(time) <= 13:
    print('lunch time')
  elif 18 <= convert(time) <= 19:
    print('dinner time')

def convert(t):
  hours, minutes = t.split(':')
  hours = int(hours)
  minutes = int(minutes)
  formatted = round(hours + minutes / 60, 2)
  return formatted

main()