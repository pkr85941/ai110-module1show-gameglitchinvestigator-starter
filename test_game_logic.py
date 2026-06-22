from logic_utils import check_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug 1: hint messages were swapped — verify correct directions
def test_too_high_message_says_go_lower():
    outcome, message = check_guess(90, 16)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_message_says_go_higher():
    outcome, message = check_guess(5, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Bug 3: secret must always be compared as int, not string
def test_no_string_comparison_large_vs_small():
    # "9" > "10" lexicographically but 9 < 10 numerically
    # if Bug 3 were present, guess=9 against secret=10 would wrongly return "Too High"
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low"


def test_no_string_comparison_two_digit():
    outcome, message = check_guess(5, 50)
    assert outcome == "Too Low"
