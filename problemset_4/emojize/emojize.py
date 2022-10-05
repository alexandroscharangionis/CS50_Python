import emoji

def main():
  emoji_code = input("Emoji code: ")
  emojize(emoji_code)

def emojize(e):
  print(emoji.emojize(e, language="alias"))

main()