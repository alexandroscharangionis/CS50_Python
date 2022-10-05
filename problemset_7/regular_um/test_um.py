from um import count
import pytest

def test_few_occurences():
  assert count('um?') == 1
  assert count('um') == 1
  assert count('Um, thanks for the album.') == 1
  assert count('Um, thanks, um...') == 2

def test_zero():
  assert count('Drums are numb') == 0
  assert count('ummmmm') == 0
  assert count('u m') == 0

def test_multiple_occurences():
  assert count('Um, even though my umbilical cord is missing, um, my umbrella is, um, better than ever, mister, (um) umpire') == 4