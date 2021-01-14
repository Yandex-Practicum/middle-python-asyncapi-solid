from abc import ABC, abstractmethod
from weapons import Laser, Karate, Gun


class AbstractHero(ABC):

    @property
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def attack(self):
        pass


class AbstractSuperHero(AbstractHero):

    @abstractmethod
    def ultimate(self):
        pass


class Superman(Karate, Laser, AbstractSuperHero):
    name = 'Clark Kent'

    def ultimate(self):
        self.incinerate_with_lasers()

    def attack(self):
        self.roundhouse_kick()
        self.ultimate()


class ChuckNorris(Gun, Karate, AbstractHero):
    name = 'Chuck Norris'

    def attack(self):
        self.roundhouse_kick()
        self.fire_a_gun()
