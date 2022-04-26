from heroes import Superman, ChuckNorris
from notifiers import TV, Newspaper
from places import Kostroma, Tokyo, Mars
from save_the_place import SavePlace

if __name__ == '__main__':
    SavePlace(Superman(), Kostroma(), TV())
    print('-' * 20)
    SavePlace(ChuckNorris(), Tokyo(), Newspaper())
    print('-' * 20)
    SavePlace(ChuckNorris(), Mars(), TV())
