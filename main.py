from abc import ABC, abstractmethod

class Weapons(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapons):
    def attack(self):
        print("Герой нанес удар мечом")
        return 2

class Bow(Weapons):
    def attack(self):
        print("Герой сделал выстрел из лука")
        return 1

class Sabre(Weapons):
    def attack(self):
        print("Герой нанес удар саблей")
        return 3