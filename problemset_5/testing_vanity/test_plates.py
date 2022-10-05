from plates import is_valid

def test_correct():
  assert is_valid('CS50') == True
  assert is_valid('BOOGIE') == True
  assert is_valid('HA') == True
  assert is_valid('JW1234') == True

def test_first_num_zero():
  assert is_valid('CS05') == False

def test_num_in_middle():
  assert is_valid('CS50P') == False

def test_punctuation():
  assert is_valid('PI3.14') == False
  assert is_valid('MY PLAT') == False
  assert is_valid('MY PLA!') == False

def test_too_short():
  assert is_valid('H') == False

def test_too_long():
  assert is_valid('OUTATIME') == False

def test_startswith_num():
  assert is_valid('57DGW') == False
  assert is_valid('88') == False
  assert is_valid('01') == False

def test_secondchar_num():
  assert is_valid('B5DK') == False

def test_empty():
  assert is_valid('') == False