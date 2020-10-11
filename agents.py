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
        """
        Function that sets a strategy to a victim. This choice is based on whether or not a gun policy is active
        :param prob_armed: boolean
        :return:
        """
        # If there is a gun policy active, there may be also a change in how an agent form his choice on strategy.
        # The rationale is that an armed agent is prone to chose react more often than an unarmed agent.
        if prob_armed:
            if self.has_gun[0]:
                self.s_victim = random.choices(['React', 'Coop'])
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
        """
        Function that verifies if the potential aggressor should star a criminal activity. This is made by checking
        the monetary units in agent's wallet
        :return: boolean
        """
        if self.wallet < 45:
            return True
        else:
            return False

    def set_strategy(self, suspicious):
        """
        Function that sets a strategy to a aggressor. This choice is based on whether or not a gun policy is active
        :param suspicious: boolean
        :return:
        """
        # The rationale is that if a gun policy is active the agent chose more often to use force as a initial strategy
        if suspicious:
            self.s_aggressor = random.choices(['Force', 'nForce'], [.7, .3])
        else:
            self.s_aggressor = random.choices(['Force', 'nForce'], [.3, .7])

    def __repr__(self):
        return f'ID: {self.unique_id}'


if __name__ == '__main__':
    pass
