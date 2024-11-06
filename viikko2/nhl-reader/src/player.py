class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        return f'{self.name:20} {self.team:6} {self.goals:2} + {self.assists:2} = {self.points}'

    @property
    def is_finnish(self):
        return self.nationality == 'FIN'

    @property
    def points(self):
        return self.goals + self.assists