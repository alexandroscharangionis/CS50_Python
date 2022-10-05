def main():
  message = input("Please say something: ")
  print(playback(message))

def playback(message):
  return message.replace(" ", "...")

main()