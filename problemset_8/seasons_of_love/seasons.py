import sys
from datetime import date
import re
import inflect

def main():
  user_date = input('Date of birth: ')
  p = inflect.engine()
  try:
    yr, month, day = check_user_birthdate(user_date)
    minutes = get_minutes_since_birth(yr, month, day)
    minutes_in_words = p.number_to_words(minutes, andword = "")
    print(f'{minutes_in_words.capitalize()} minutes')
  except:
    sys.exit('Invalid date')


def get_minutes_since_birth(yr, mth, day):
  today_date = date.today()
  user_birth_date = date(int(yr), int(mth), int(day))
  total_days = today_date - user_birth_date
  total_minutes = total_days.days * 24 * 60
  return total_minutes

def check_user_birthdate(d):
  if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", d):
    yr, month, day = d.split('-')
    return yr, month, day


if __name__ == '__main__':
  main()