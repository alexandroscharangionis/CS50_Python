def main():
  text = input("Type something: ")
  remove_vowels(text)

def remove_vowels(t):
  devoweled = ''
  for character in t:
    lowered = character.lower()
    match lowered:
      case 'a' | 'e' | 'i' | 'o' | 'u':
        devoweled +=''
      case _:
        devoweled += character

  print(devoweled)

main()
