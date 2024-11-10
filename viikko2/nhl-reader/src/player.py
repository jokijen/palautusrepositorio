class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.team = player_dict['team']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']
    
    def __str__(self):
        return f'{self.name:25} {self.team:8} {self.goals:3} + {self.assists:2} = {self.points}'

    @property
    def points(self):
        return self.goals + self.assists
    
    def is_nationality(self, nationality):
        return self.nationality == nationality
