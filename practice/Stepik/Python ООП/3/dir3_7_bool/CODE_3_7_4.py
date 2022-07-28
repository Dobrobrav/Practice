class Player:
    name: str
    old: int
    score: int

    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0

    def __repr__(self):
        return f"{self.name}-{self.old}-{self.score}"


if __name__ == '__main__':
    lst_in = [
        'Балакирев; 34; 2048',
        'Mediel; 27; 0',
        'Влад; 18; 9012',
        'Nina P; 33; 0',
    ]

    players = [
        Player(record.split('; ')[0], *(int(e) for e in record.split('; ')[1:3]))
        for record in lst_in
    ]

    players_filtered = list(filter(bool, players))

    print(players)
    print(players_filtered)
