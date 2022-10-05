def main():
  variable_name = input("Insert camel-case variable: ")
  camel_snake_converter(variable_name)

def camel_snake_converter(varname):
  snake_string = ''
  for character in varname:
    if character.isupper():
      snake_string += '_'
    snake_string += character.lower()
  print(snake_string)

main()