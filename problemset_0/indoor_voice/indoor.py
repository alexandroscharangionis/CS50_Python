def main():
  message = input("What would you like to say? ")
  print(indoorVoice(message))

def indoorVoice(message):
  return message.lower()

main()