from places import Kostroma, Tokyo

class AntagonistFinder:
    # Проблема: Класс, отвечающий за вызов верного метода у классов разного типа добавляет излишнюю сложность
    # Несоблюден: Принцип инверсии зависимостей
    # По SOLID: Создать абстрактный класс Place, обязывающий реализовать метод для поиска злодея
    # Когда возникнут трудности: Когда ваш проект обретет мировую славу

    def get_antagonist(self, place):
        if isinstance(place, Kostroma):
            place.get_orcs()
        elif isinstance(place, Tokyo):
            place.get_godzilla()
