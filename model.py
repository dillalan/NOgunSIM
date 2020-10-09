from agents import Victim
from agents import Aggressor
import random


class GunSIM:
    def __init__(self):
        self.policy = True
        self.victims = list()
        self.muggers = list()
        self.grow_victims()
        self.grow_robbers()
        self.step()

    def grow_victims(self, n=200):
        """
        Function that generates agents Victims
        :param n: number of agents of this type
        :return:
        """
        for i in range(n):
            self.victims.append(Victim(unique_id=i))
            if self.policy:
                for v in range(len(self.victims)):
                    self.victims[i].has_gun = random.choices([True, False], [.1, .9])

    def grow_robbers(self, n=10):
        """
        Function that generates the agents Aggressors
        :param n: number of agents of this type
        :return:
        """
        for i in range(n):
            self.muggers.append(Aggressor(unique_id=i))

    def theory_moves(self, victim, mugger):
        """
        A function that change the agent's strategy based on Theory of Moves from Steven Brams(1993)
        :param victim:
        :param mugger:
        :return:
        """
        if mugger.s_aggressor[0] == 'Force' and victim.s_victim[0] == 'Coop':
            victim.s_victim[0] = random.choice(['Coop', 'React'])
        if mugger.s_aggressor[0] == 'nForce' and victim.s_victim[0] == 'React':
            victim.s_victim[0] = random.choice(['Coop', 'React'])
            if victim.s_victim[0] == 'React':
                mugger.s_aggressor[0] = random.choice(['nForce', 'Force'])
        self.mugging_game(victim, mugger)

    def mugging_game(self, victim, mugger):
        """
        The payoff results from Mugging Game by Steven Brams(1993)
        :param victim:
        :param mugger:
        :return:
        """
        # I Fight: (2,2). The victim resists, and the mugger uses force. The mugger gets the victim's money but may
        # attract attention, whereas the victim is injured and loses its money. Nonetheless, the victim has achieved
        # its tertiary goal of increasing the probability of the mugger's arrest.
        if victim.s_victim[0] == 'React' and mugger.s_aggressor[0] == 'Force':
            mugger.wallet += victim.wallet
            if random.choice(['survive', 'perish']) == 'perish':
                self.victims.remove(victim)
            if random.choices(['flew', 'caught'], [.7, .3]) == 'caught':
                self.muggers.remove(mugger)
        # II Mugger fails: (4, 1). The victim resists the mugger, who is frightened away, and achieves all its goals.
        # The mugger achieves only its tertiary goal.
        if victim.s_victim[0] == 'React' and mugger.s_aggressor[0] == 'nForce':
            if random.choices(['flew', 'caught'], [.7, .3]) == 'caught':
                self.muggers.remove(mugger)
        # III Voluntary submission: (3,4). The victim gives up its money, and the mugger leaves the victim
        # unharmed. The mugger achieves all its goals, whereas the victim achieves its primary goal of escaping
        # unharmed.
        if victim.s_victim[0] == 'Coop' and mugger.s_aggressor[0] == 'nForce':
            mugger.wallet += victim.wallet
        # IV Involuntary submission: ( 1 ,3). The victim gives up its money, but the mugger uses force anyway. The
        # victim achieves none of its goals, whereas the mugger achieves its two most important goals, sacrificing
        # only its tertiary goal by taking a greater risk of getting caught.
        if victim.s_victim[0] == 'Coop' and mugger.s_aggressor[0] == 'nForce':
            mugger.wallet += victim.wallet
            if random.choices(['survive', 'perish'], [.9, .1]) == 'perish':
                self.victims.remove(victim)
            if random.choices(['flew', 'caught'], [.7, .3]) == 'caught':
                self.muggers.remove(mugger)

    def step(self):
        """
        A function where the interaction of agents
        :return:
        """
        for victim in self.victims:
            match = random.choice(['bad_guy', 'other', None])
            if match == 'bad_guy':
                mugger = random.choice(self.muggers)
                if mugger.is_active:
                    mugger.set_strategy(suspicious=self.policy)
                    victim.set_strategy(self.policy)
                    self.theory_moves(victim, mugger)


if __name__ == '__main__':
    r = GunSIM()