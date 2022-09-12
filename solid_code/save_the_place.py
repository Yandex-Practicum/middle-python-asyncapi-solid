from heroes import AbstractHero
from places import AbstractPlace
from notifiers import AbstractNotifier


class SavePlace:

    def find_enemy(self):
        return self.place.get_antagonist()

    def notify(self):
        self.notifier.publicize(f'{self.hero.name} saved the {self.place.name}!')

    def __init__(self, hero: AbstractHero, place: AbstractPlace, notifier: AbstractNotifier):
        self.place = place
        self.hero = hero
        self.notifier = notifier

        self.find_enemy()
        self.hero.attack()
        self.notify()
