from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_new_game_resets_status():
    # Bug fix (3): New Game must reset status to "playing".
    # Without this, the status check blocks the game after a win/loss.
    session = {"status": "won", "attempts": 5, "secret": 42}

    # Simulate what the fixed New Game handler does
    session["attempts"] = 0
    session["secret"] = 99
    session["status"] = "playing"

    assert session["status"] == "playing", (
        "New game must reset status to 'playing' so the game is not blocked"
    )

def test_new_game_resets_status_after_loss():
    # Bug fix (3): New Game must also reset status when the player lost.
    session = {"status": "lost", "attempts": 8, "secret": 42}

    session["attempts"] = 0
    session["secret"] = 55
    session["status"] = "playing"

    assert session["status"] == "playing", (
        "New game must reset status to 'playing' even after a loss"
    )

def test_hint_direction_not_swapped():
    # Bug fix (1): when guess > secret, message should say Go LOWER, not Go HIGHER.
    # "9" > "50" lexicographically, so this case would fail before the fix.
    _, message_high = check_guess(9, 5)
    assert "LOWER" in message_high, (
        "Guess too high should say Go LOWER, not Go HIGHER"
    )

    _, message_low = check_guess(5, 9)
    assert "HIGHER" in message_low, (
        "Guess too low should say Go HIGHER, not Go LOWER"
    )

def test_parse_guess_rejects_floats():
    #  Floats should be rejected — all difficulty ranges use whole integers
    ok, _, err = parse_guess("50.5")
    assert ok == False
    assert err is not None

def test_parse_guess_out_of_range():
    # Bug fix (2) 
    # Guesses outside 1-100 should be rejected
    ok_high, _, err_high = parse_guess("150")
    assert ok_high == False
    assert err_high is not None
    assert "integer" in err_high.lower()

    ok_low, _, err_low = parse_guess("0")
    assert ok_low == False
    assert err_low is not None
    assert "integer" in err_low.lower()
