from typing import Union
from heroes import Superman, SuperHero
from places import Kostroma, Tokyo


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo]):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    hero.create_news(place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(SuperHero('Chack Norris', False), Tokyo())
