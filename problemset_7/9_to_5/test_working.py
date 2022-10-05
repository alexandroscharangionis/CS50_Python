from working import convert
import pytest

def test_correct():
  assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_errors_num():
  with pytest.raises(ValueError):
    convert('9:60 AM to 5:60 PM')
  with pytest.raises(ValueError):
    convert('9 AM - 5 PM')

def test_errors_char():
  with pytest.raises(ValueError):
    convert('nine AM to four PM')