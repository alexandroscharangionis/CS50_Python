import sys
from PIL import Image, ImageOps
import os

def main():
  check_cmd_args_len()
  check_cmd_args_ext()
  edit_img()

def edit_img():
  try:
    with Image.open(sys.argv[1]) as muppet, Image.open("shirt.png") as shirt:
      resized = ImageOps.fit(muppet, size=shirt.size)
      resized.paste(shirt, shirt)
      resized.save(sys.argv[2])
  except FileNotFoundError:
    sys.exit('Input does not exist')

def check_cmd_args_len():
  if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
  elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

def check_cmd_args_ext():
  extensions = ['.jpg', '.jpeg', '.png']
  for arg in sys.argv[1:]:
    if not arg.endswith(extensions[0]) and not arg.endswith(extensions[1]) and not arg.endswith(extensions[2]):
      sys.exit('Invalid output')

  if sys.argv[1].split('.')[1] != sys.argv[2].split('.')[1]:
    sys.exit('Input and output have different extensions')

if __name__ == '__main__':
  main()