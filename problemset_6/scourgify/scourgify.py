import sys
import csv

def main():
  clean_file()

def clean_file():
  if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
  elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
  else:
    students = []
    try:
      with open(sys.argv[1]) as original_file:
        dictreader = csv.DictReader(original_file)
        for row in dictreader:
          last, first = row['name'].split(',')
          student = {'first': first.lstrip(), 'last': last, 'house': row['house']}
          students.append(student)
        with open(sys.argv[2], 'w') as updated_file:
          fieldnames = ['first', 'last', 'house']
          writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
          writer.writeheader()
          for student in students:
            writer.writerow(student)
    except FileNotFoundError:
      sys.exit(f'Could not read {sys.argv[1]}')

if __name__ == '__main__':
  main()