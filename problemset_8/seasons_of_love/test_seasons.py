from seasons import check_user_birthdate, get_minutes_since_birth
import pytest

def test_user_input():
  assert check_user_birthdate('1994-5-7') == None
  assert check_user_birthdate('1994-04-22') == ('1994', '04', '22')

def test_minutes_since_birth():
  assert get_minutes_since_birth('1994', '04', '22') == 14958720