from abc import ABC, abstractmethod


class AbstractPlace(ABC):

    @property
    def name(self):
        raise NotImplementedError

    @abstractmethod
    def get_antagonist(self):
        pass


class Kostroma(AbstractPlace):
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(AbstractPlace):
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Mars(AbstractPlace):

    coordinates = [13, 4]

    @property
    def name(self):
        return ','.join(map(str, self.coordinates))

    def get_antagonist(self):
        print('Aliens abduct cows in the meadow')
