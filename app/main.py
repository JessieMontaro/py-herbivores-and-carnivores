class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        Animal.alive.append(self)
        self.hidden = False

    def __repr__(self) -> str:
        status = {
            "Name": self.name, "Health": self.health, "Hidden": self.hidden
        }
        return str(status).replace("\'", "")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, bitee) -> None:
        if isinstance(bitee, Herbivore) and not bitee.hidden:
            bitee.health -= 50
            print(f"{bitee.name} is bitten")
            if bitee.health <= 0:
                Animal.alive.remove(bitee)
