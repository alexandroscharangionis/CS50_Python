import inflect
p = inflect.engine()

def main():
  name_list = []
  while True:
    try:
      name = input('Name: ')
      name_list.append(name)
    except EOFError:
      joined = p.join(name_list)
      print(f'Adieu, adieu, to {joined}')
      break

main()