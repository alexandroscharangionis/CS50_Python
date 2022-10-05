def main():
  text = input("Type something: ")
  print(shorten(text))

def shorten(word):
  devoweled = ''
  for character in word:
    lowered = character.lower()
    match lowered:
      case 'a' | 'e' | 'i' | 'o' | 'u':
        devoweled += ''
      case _:
        devoweled += character

  return devoweled

if __name__ == '__main__':
  main()