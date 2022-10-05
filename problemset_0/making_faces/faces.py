def main():
  message = input("Say something: ")
  print(convert(message))

def convert(message):
  return message.replace(":)", "🙂").replace(":(", "🙁")

main()