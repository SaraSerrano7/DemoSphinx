"""
Librería de Python para que un perro ladre y decir Hello world
"""


class Dog:
    """
    Clase de Python para modelar un perro.
    """

    def __init__(self, race):
        """

        Para instanciar a un perro de una raza concreta.

        :param race: Raza del perro.
        :type race: str
        """
        self.race = race

    def print_race(self):
        """

        Imprime la raza del perro

        :return: None
        """
        print(self.race)

    @staticmethod
    def bark(num):
        """

        El perro ladra tantas veces como indice "num".

        :param num: Numero de veces que el perro ladra.
        :type num: int.
        :raise main.Dog.TypeError: Si el parametro es invalido.
        :return: Una lista con tantos ladridos como num indique.
        :rtype: list[str].
        """
        barks = []
        for _ in range(num):
            barks.append('Woof')
        return barks


if __name__ == '__main__':
    gus = Dog('Maltese')
    gus.print_race()
    gus.bark('a')


def hello_world(name):
    """

    Una persona dice hello world

    :param name: Nombre de la persona que dice Hello World
    :type name: str
    :return: El mensaje de una persona que dice Hello world
    :rtype: str
    """
    return f'{name} says Hello World!'
