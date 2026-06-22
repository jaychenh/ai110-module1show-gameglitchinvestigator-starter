from logic_utils import get_range_for_difficulty, check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in msg


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, msg = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in msg


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in msg


def test_get_range_for_difficulty_hard():
    # Hard difficulty should use the correct number range for a new game
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100


def test_parse_guess_invalid():
    # Non-numeric input should fail parsing and return a helpful error
    ok, value, error = parse_guess("abc")
    assert ok is False
    assert value is None
    assert error == "That is not a number."
