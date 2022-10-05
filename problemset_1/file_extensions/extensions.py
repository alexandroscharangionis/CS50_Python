def main():
  file_name = input("What's the name of your file? ").lower().strip().split('.')[-1]
  printFileType(file_name)

def printFileType(file):
  match file:
    case 'gif':
      print('image/gif')
    case 'jpg' | 'jpeg':
      print('image/jpeg')
    case 'png':
      print('image/png')
    case 'pdf':
      print('application/pdf')
    case 'txt':
      print('text/plain')
    case 'zip':
      print('application/zip')
    case _:
      print('application/octet-stream')

main()
