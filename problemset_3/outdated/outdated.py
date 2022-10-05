def main():
  while True:
    date = input("Date: ")
    if format_date(date):
      print(format_date(date))
      break

def check_date_validity(m, d, months_list):
  if len(m) < 3:
    if int(m) > 12 or int(m) < 1 or int(d) > 31 or int(d) < 1:
      return False
    else:
      return True
  else:
    return m in months_list

def format_date(d):
  months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
  if '/' in d:
    month, day, year = d.split('/')
    if len(month) > 2:
      return False
  else:
    month, day, year = d.split()
    if not ',' in day or len(day) > 2:
      return False
    else:
      day = day[0:-1]
      month = str(int(months.index(month)) + 1)

  if check_date_validity(month, day, months):
    formatted = f'{int(year)}-{int(month):02}-{int(day):02}'
    return formatted
  else:
    return False

main()