from numb3rs import validate

def test_single_digits():
  assert validate('1.9.5.0') == True
  assert validate('1.449.5.0') == False
  assert validate('7.1.0.0') == True
  assert validate('8.3.2') == False
  assert validate('8') == False

def test_double_digits():
  assert validate('10.99.25.36') == True
  assert validate('10.499.25.36') == False
  assert validate('82.75.22') == False
  assert validate('82.22') == False
  assert validate('82') == False

def test_three_digits():
  assert validate('255.255.255.255') == True
  assert validate('256.255.255.255') == False
  assert validate('435.255.255.255') == False
  assert validate('256.258.255.255') == False
  assert validate('435.255.255') == False
  assert validate('255') == False

def test_random():
  assert validate('cat') == False
  assert validate('1043.209.2.45') == False
  assert validate('43.2099.2.45') == False
  assert validate('43.99.2555.45') == False
  assert validate('43.99.34.745') == False
