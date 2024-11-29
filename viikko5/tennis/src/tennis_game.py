class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        # Player 1 wins point
        if player_name == self.player1:
            self.player1_points += 1
        # Player 2 wins point
        else:
            self.player2_points += 1

    def get_score(self):
        if self.player1_points == self.player2_points:
            return self._get_even_score()

        elif self.player1_points >= 4 or self.player2_points >= 4:
            return self._get_advantage_or_win_score()
        
        else:
            return self._get_regular_score()


    def _get_even_score(self):
        score_dict = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        if self.player1_points in score_dict:
            return score_dict[self.player1_points]
        
        # If the game is tied with 3 or more points each, the score is always called "Deuce"
        else:
            return "Deuce"
        
    def _get_advantage_or_win_score(self):
        point_difference = self.player1_points - self.player2_points

        if point_difference == 1:
            return "Advantage player1"
        elif point_difference == -1:
            return "Advantage player2"
        elif point_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_regular_score(self):
        point_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
            }
        
        return f"{point_names[self.player1_points]}-{point_names[self.player2_points]}"
