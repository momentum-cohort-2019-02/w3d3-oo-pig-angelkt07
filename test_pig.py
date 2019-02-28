from pig import ComputerPlayer

def test_ComputerPlayer():
    name_player = ComputerPlayer("Kasey")
    assert str(name_player) == "Kasey"


# def test_random_roll():
#     assert random.side in ['1', '2', '3', '4', '5', '6']


# """
# Ideas for tests:

# method "Hold"
#     - does it return the next player
#     - does it return a new score total
#     - does it increase the turn count

# method "turn"
#     - if count = 0, does it choose "R" for roll
#     - if count > 0, does it give the next option.

# method or class dice:
#     - does it pull a range of 1 -6

# method roll
#     - does it return a random number less then 6
# """