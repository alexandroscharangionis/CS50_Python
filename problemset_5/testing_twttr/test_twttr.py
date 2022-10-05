from twttr import shorten

def test_uppercase():
  assert shorten('HAHA') == 'HH'

def test_lowercase():
  assert shorten('meme') == 'mm'

def test_randomcase():
  assert shorten('HAhezIhOhfuU') == 'Hhzhhf'

def test_mixed():
  assert shorten('Dedmau5') == 'Ddm5'

def test_empty():
  assert shorten('') == ''

def test_punctuation():
  assert shorten('Aki, hello there') == 'k, hll thr'