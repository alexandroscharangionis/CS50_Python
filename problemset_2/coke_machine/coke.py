def main():
  vending_machine()

def vending_machine():
  price = 50
  inserted_amount = 0

  while True:
    if inserted_amount >= price:
      print(f'Change owed: {inserted_amount - price}')
      break
    print(f'Amount due: {price - inserted_amount}')
    coins = int(input("Insert coins: "))
    if coins == 5 or coins == 10 or coins == 25:
      inserted_amount += coins
    else:
      continue

main()


