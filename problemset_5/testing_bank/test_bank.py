from bank import value

def test_integers():
  assert value('4') == 100

def test_negative_integers():
  assert value('-5') == 100

def test_empty():
  assert value('') == 100

def test_hello():
  assert value('hello') == 0

def test_hi():
  assert value('hi') == 20

def test_random():
  assert value('guten tag') == 100

def test_case_insensitivity():
  assert value('HeLlo') == 0
  assert value('hI tHere') == 20
  assert value('goOD aFTerNooN') == 100