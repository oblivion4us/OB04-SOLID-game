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

class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon
        self.health = 5  # Количество жизней у Fighter

    def change_weapon(self, new_weapon_type):
        current_weapon_name = type(self.weapon).__name__
        if new_weapon_type == "Sword" and not isinstance(self.weapon, Sword):
            self.weapon = Sword()
            print(f"Герой сменил {current_weapon_name} на Sword")
        elif new_weapon_type == "Bow" and not isinstance(self.weapon, Bow):
            self.weapon = Bow()
            print(f"Герой сменил {current_weapon_name} на Bow")
        elif new_weapon_type == "Sabre" and not isinstance(self.weapon, Sabre):
            self.weapon = Sabre()
            print(f"Герой сменил {current_weapon_name} на Sabre")
        else:
            print(f"Герой уже вооружен {current_weapon_name.lower()} или неверный тип оружия")

    def attack(self, monster):
        damage = self.weapon.attack()
        monster.take_damage(damage)

class Monsters(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона. Осталось жизней: {self.health}")
        if self.health <= 0:
            print(f"{self.name} побежден!")

class Monster(Monsters):
    def __init__(self, health=2):  # По умолчанию у монстра 2 жизни
        super().__init__("Монстр", health)

class Boss(Monsters):
    def __init__(self):
        super().__init__("Босс", 10)  # У босса 10 жизней

fighter1 = Fighter(Sword())
monster1 = Monster()
boss1 = Boss()
monster3 = Monster(health=5)

fighter1.attack(monster1)
fighter1.change_weapon("Sabre")
fighter1.attack(monster3)
fighter1.attack(monster3)

fighter1.attack(boss1)
fighter1.attack(boss1)
fighter1.attack(boss1)
fighter1.change_weapon("Bow")
fighter1.attack(boss1)