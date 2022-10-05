import re

def main():
  print(count(input('Text: ')))

def count(s):
  s = s.strip().lower()
  if matches := re.findall(r"\bum\b", s):
    return len(matches)
  else:
    return 0

if __name__ == '__main__':
  main()
