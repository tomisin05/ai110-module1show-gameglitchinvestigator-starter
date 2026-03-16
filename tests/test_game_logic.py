from logic_utils import check_guess, parse_guess, get_range_for_difficulty

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# FIX verification: confirm hint messages point in the correct direction
def test_too_high_message_says_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok is True and value == 42 and err is None

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False and value is None

def test_parse_guess_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False

def test_get_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_get_range_hard_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high
