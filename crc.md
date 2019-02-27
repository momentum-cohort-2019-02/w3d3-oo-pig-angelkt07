PIG CRC Model

Class ComputerPlayer(self):
    - will need individual score throughout game
    - if ComputerPlayerScore <= 20 and roll != 1:
        then "H" for Hold
        elif ComputerPlayerScore > 20 and roll != 1:
            then randomly select R or H
        else roll = 1:
            then next player
            

Class HumanPlayer(self):
will need individual score throughout game
first turn - roll
    if random.roll = 1
        then 0 points
        change to ComputerPlayer
    else random.roll > 1
        option to hold or roll
            if hold
                then add points to "New Score" for HumanPlayer
            else roll
                return random.roll

Class FirstPlayer(self):
    if first player = Computer
        then rotate.

Class NextPlayer?? or have method in turn class to rotate players

Class Score(self):
    self.score = score
    self.new_score = new_score
    self.score(start_score=0)

Class RandomRoll(self)
    if user selects "R" for roll, 
        then select random side of Class Dice
    else user selected "H" for hold:
        then add current_total_of_points + new_score


Class Dice(self)
    self.sides = sides

    def side(self):
    side = (1:6)

return side

Class Turn(self):
    if score >= 100:
        game over
        declare winner
    else:
        keep_playing and rotate player