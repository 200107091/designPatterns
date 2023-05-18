from abc import ABC, abstractmethod

class AttackStrategy(ABC):
    """
    Интерфейс
    """
    @abstractmethod
    def attack(self):
        pass

class SwordAttack(AttackStrategy):
    """
    Класс для атаки врага с помощью рубящего удара мечом
    """
    def attack(self):
        print("Attacking with a sword.")

class AxeAttack(AttackStrategy):
    """
    Класс для атаки врага рубящим топором
    """
    def attack(self):
        print("Attacking with an axe.")

class BowAttack(AttackStrategy):
    """
    Класс для атаки врага с помощью стрельбы из лука и стрел
    """
    def attack(self):
        print("Attacking with a bow and arrow.")

class Player:
    """
    қаруларды таңдау
    """
    def __init__(self, attack_strategy):
        self.attack_strategy = attack_strategy

    def set_attack_strategy(self, attack_strategy):
        self.attack_strategy = attack_strategy

    def attack(self):
        self.attack_strategy.attack()

sword_attack = SwordAttack()
axe_attack = AxeAttack()
bow_attack = BowAttack()

#output
player = Player(sword_attack)
player.attack()  

#output
player.set_attack_strategy(axe_attack)
player.attack()  



class MagicAttack:
    """
    Класс для атаки врага магией
    """
    def attack(self):
        print("Attacking with magic.")

magic_attack = MagicAttack()

#output
player = Player(magic_attack)
player.attack() 