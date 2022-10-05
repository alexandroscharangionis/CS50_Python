def main():
  create_grocery_list()

def create_grocery_list():
  grocery_list = {}
  while True:
    try:
      item = input().upper()
      if not grocery_list.get(item):
        grocery_list[item] = 1
      else:
        grocery_list[item] = grocery_list[item] + 1
    except EOFError:
      print()
      break
  for grocery_item in sorted(grocery_list):
    print(f'{grocery_list[grocery_item]} {grocery_item}')

main()

