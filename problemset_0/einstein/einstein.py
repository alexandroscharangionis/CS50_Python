def main():
  mass = int(input("Choose number of kg: "))
  print(f"Total number of Joules is {getJoules(mass)}")

def getJoules(kg):
  return round(kg * 300000000**2)

main()