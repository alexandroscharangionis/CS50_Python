from fuel import convert, gauge
import pytest

def test_correct_return_value():
  assert convert('2/3') == 67
  assert convert('3/3') == 100
  assert convert('1/99') == 1
  assert convert('1/100') == 1
  assert gauge(1) == 'E'
  assert gauge(99) == 'F'
  assert gauge(73) == '73%'

def test_raised_errors():
  with pytest.raises(ZeroDivisionError):
    convert('5/0')
  with pytest.raises(ValueError):
    convert("sd")
    convert("s/d")
    convert("s/50")
  with pytest.raises(ValueError):
    convert("-5/10")
    convert("5/-3")
    convert("1.5/3")
    convert("5/3")

