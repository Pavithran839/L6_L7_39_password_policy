import pytest
from password_policy import check_password, strength, suggest_fix


# Core tests (same as code coverage file)
def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []

def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"

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

def test_strength_strong():
    assert strength("Abcdefghijkl1!") == "strong"

def test_strength_weak():
    assert strength("Abcdefg1") == "weak"

def test_strength_very_weak():
    assert strength("abc") == "very weak"

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


# Extra branch and boundary tests
def test_length_boundary_8_is_not_too_short():
    issues = check_password("Abcdef1!")
    assert "too short" not in issues and "too long" not in issues

def test_length_boundary_7_is_too_short():
    assert "too short" in check_password("Abcde1!")

def test_length_boundary_64_is_not_too_long():
    pw = "Aa1!" + "a" * 60
    assert len(pw) == 64
    assert "too long" not in check_password(pw)

def test_length_boundary_65_is_too_long():
    pw = "Aa1!" + "a" * 61
    assert len(pw) == 65
    assert "too long" in check_password(pw)

def test_common_password_case_insensitive():
    assert "common" in check_password("PASSWORD")

def test_non_common_password_has_no_common_issue():
    assert "common" not in check_password("Abcdef1!")

def test_strength_boundary_13_is_good():
    pw = "Abcdefghijk1!"
    assert len(pw) == 13
    assert strength(pw) == "good"

def test_strength_boundary_14_is_strong():
    pw = "Abcdefghijkl1!"
    assert len(pw) == 14
    assert strength(pw) == "strong"

def test_strength_two_issues_is_weak():
    # "abcdefgh" -> no uppercase, no digit, no special = 3 issues
    # "abcdefg1!" -> no uppercase only = 1 issue
    assert strength("abcdefg1!") == "weak"

def test_strength_three_issues_is_very_weak():
    assert strength("abcdefgh") == "very weak"

def test_empty_password():
    issues = check_password("")
    assert "too short" in issues
    assert "no uppercase" in issues
    assert "no lowercase" in issues
    assert "no digit" in issues
    assert "no special" in issues

def test_suggest_fix_uses_first_issue_only():
    assert suggest_fix(["no uppercase", "no digit"]) == "add uppercase"

def test_suggest_fix_no_special():
    assert suggest_fix(["no special"]) == "add special"
