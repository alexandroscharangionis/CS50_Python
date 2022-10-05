import re

def main():
  print(validate(input('IPv4 Address: ')))

def validate(ip):
  ip = ip.strip()
  if matches := re.search(r"^(?:(?:2(?:[0-5][0-5]|[0-4]\d)|1\d\d|[1-9]\d|\d)\.){3}(?:2[0-5][0-5]|1\d\d|[1-9]\d|\d)$", ip, re.ASCII):
    return True
  else:
    return False

if __name__ == '__main__':
  main()