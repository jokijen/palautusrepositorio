class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        return f'{self.name}, team {self.team}, goals {self.goals}, assists {self.assists}'

    def is_finnish(self):
        return self.nationality == 'FIN'
