import random


class Victim:

    def __init__(self, unique_id, has_gun=None):
        self.unique_id = unique_id
        self.wallet = random.randint(50, 100)
        self.has_gun = has_gun
        self.s_victim = None

    def __repr__(self):
        return f'{self.unique_id}'

    def set_strategy(self, prob_armed):
        if prob_armed:
            if self.has_gun[0]:
                self.s_victim = random.choice(['React', 'Coop'])
            else:
                self.s_victim = random.choices(['React', 'Coop'], [.2, .8])
        else:
            self.s_victim = random.choices(['React', 'Coop'], [.2, .8])


class Aggressor:

    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.wallet = random.randint(10, 50)
        self.s_aggressor = None

    def is_active(self):
        if self.wallet < 20:
            return True

    def set_strategy(self, suspicious):
        if suspicious:
            self.s_aggressor = random.choices(['Force', 'nForce'], [.7, .3])
        else:
            self.s_aggressor = random.choices(['Force', 'nForce'], [.3, .7])

    def __repr__(self):
        return f'ID: {self.unique_id}'


if __name__ == '__main__':
    Carlos = Aggressor(1)
    Carlos.set_strategy(False)
    print(Carlos.s_aggressor)
    print(Carlos.s_aggressor[0])

