from pyfiglet import Figlet
import random
import sys
figlet = Figlet()

def main():
  set_font_or_quit()
  text = input("Your text: ")
  print(figlet.renderText(text))

def set_font_or_quit():
  fonts = figlet.getFonts()
  if len(sys.argv) == 1:
    random_int = random.randint(0, len(fonts))
    figlet.setFont(font = fonts[random_int])
  elif len(sys.argv) == 2:
    sys.exit('Too few arguments')
  elif len(sys.argv) == 3:
    if sys.argv[1] != '--font' and sys.argv[1] != '-f' or sys.argv[2] not in fonts:
      sys.exit('Something went wrong')
    else:
      figlet.setFont(font = sys.argv[2])

main()