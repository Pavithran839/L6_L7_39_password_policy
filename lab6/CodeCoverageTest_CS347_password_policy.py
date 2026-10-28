import pytest
from password_policy import check_password, strength, suggest_fix


# Given examples
def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []

def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"


# check_password
def test_too_short():
    assert "too short" in check_password("Ab1!")

def test_too_long():
    assert "too long" in check_password("Aa1!" + "a" * 61)

def test_common_password():
    assert "common" in check_password("password")

def test_no_uppercase():
    assert "no uppercase" in check_password("abcdef1!")

def test_no_lowercase():
    assert "no lowercase" in check_password("ABCDEF1!")

def test_no_digit():
    assert "no digit" in check_password("Abcdefg!")

def test_no_special():
    assert "no special" in check_password("Abcdefg1")


# strength
def test_strength_strong():
    assert strength("Abcdefghijkl1!") == "strong"

def test_strength_weak():
    assert strength("Abcdefg1") == "weak"

def test_strength_very_weak():
    assert strength("abc") == "very weak"


# suggest_fix
def test_suggest_fix_none():
    assert suggest_fix([]) == "none needed"

def test_suggest_fix_too_short():
    assert suggest_fix(["too short"]) == "add more characters"

def test_suggest_fix_common():
    assert suggest_fix(["common"]) == "avoid common passwords"

def test_suggest_fix_missing_char_type():
    assert suggest_fix(["no digit"]) == "add digit"

def test_suggest_fix_fallback():
    assert suggest_fix(["too long"]) == "shorten it"
