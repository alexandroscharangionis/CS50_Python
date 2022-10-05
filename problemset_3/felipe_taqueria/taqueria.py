def main():
  order_food()

def order_food():
  total_price = 0
  menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
  while True:
    try:
      order = input('Item: ').lower().title()
      if menu[order]:
        total_price += menu[order]
        print(f'Total: ${total_price:.2f}')
    except KeyError:
      pass
    except EOFError:
      print()
      break
main()