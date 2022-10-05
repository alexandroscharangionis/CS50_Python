import re

def main():
  print(parse(input("HTML: ")))

def parse(s):
  s = s.strip()
  if link_matches := re.search(r"src=\"(.+)\"", s):
    s = link_matches.group(1)
  else:
    return None

  if matches := re.search(r"^(?:https?:\/\/)?(?:www\.)?youtube.com\/embed\/([a-zA-Z0-9_]+)$", s):
    formatted = f'https://youtu.be/{matches.group(1)}'
    return formatted

if __name__ == '__main__':
  main()