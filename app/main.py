class Animal:

    alive: list["Animal"] = []

    def __init__(self, name: str, *args) -> None:
        self.name = name
        if args != ():
            self.health = args[0]
        else:
            self.health = 100
        Animal.alive.append(self)
        self.hidden = False

    def __repr__(self) -> str:
        represent = (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )
        return represent


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            print(f"{prey.name} is bitten")
            if prey.health <= 0:
                Animal.alive.remove(prey)
