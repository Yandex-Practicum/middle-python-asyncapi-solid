from abc import ABC, abstractmethod


class AbstractNotifier(ABC):
    @abstractmethod
    def publicize(self, text):
        pass


class Newspaper(AbstractNotifier):
    def publicize(self, text):
        print(f'Today in newspaper: {text}')


class TV(AbstractNotifier):
    def publicize(self, text):
        print(f'Watch on the first channel: {text}')