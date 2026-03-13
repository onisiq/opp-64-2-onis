
class Hero:
    """создан класс и его подклассы"""
    def __init__(self,name,level,health,strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    
    def greet(self):
        print(f'Привет, я {self.name}, мой уровень:{self.level}')
    
    def attack(self):
        print(f'{self.name} Атакует!')

    def rest(self):
        print(f'{self.name} Отдыхает!')
        self.health += 1
        print(f'{self.name} здоровье увеличилось до {self.health} ')       
    
class Warrior(Hero):
    def __init__(self, name, level, health, strength,stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f'{self.name} атакует мечом!')
        self.stamina -= 1
        print(f'{self.name} герой устал {self.stamina}')
        
    
class Mage(Hero):
    def __init__(self, name, level, health, strength,mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    
    def attack(self):
        print(f'{self.name} использует магию!')
        self.mana -= 1
        print(f'{self.name} герой потратил {self.mana}')
        

class Assassin(Hero):
    def __init__ (self,name,level,health,strength,stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    
    def attack(self):
        print(f'{self.name} использует скрытность!')
        self.stealth -= 1
        print(f'{self.name} герой потратил {self.stealth}')
        

def fight(player, enemy):
    """создана функция которая выбирает кто выиграл взамисимости от выбора игрока и бота"""
    if isinstance(player, Warrior) and isinstance(enemy, Assassin):
        return "Player win"

    elif isinstance(player, Assassin) and isinstance(enemy, Mage):
        return "Player win"

    elif isinstance(player, Mage) and isinstance(enemy, Warrior):
        return "Player win"

    elif type(player) == type(enemy):
        return "Draw"

    else:
        return "Enemy win"

#проверка первого часть кода
Kratos = Warrior("Kratps",100,1000,100,50)
Kratos.greet()
Kratos.attack()
Kratos.rest()

Harry_Potter = Mage("Harry Potter", 80, 800, 80, 200)
Harry_Potter.greet()
Harry_Potter.attack()
Harry_Potter.rest()

agent_007 = Assassin("Agent 007", 90, 900, 90, 70)
agent_007.greet()
agent_007.attack()
agent_007.rest()

#использован random для рандома
import random

Heroes= [
        Warrior("Enemy Warrior",1,100,10,5),
        Mage("Enemy Mage",1,80,12,10),
        Assassin("Enemy Assassin",1,90,11,7)
]

    
enemy = random.choice(Heroes)#рандомно выбирает от 1 до 3 обьект
choice = input("Выберите героя Warrior, Mage, Assassin: ").capitalize()#без разницы Б или М

if choice == "Warrior":
        player = Warrior("Player Warrior",1,100,10,5)

elif choice == "Mage":
        player = Mage("Player Mage",1,80,12,10)

elif choice == "Assassin":
        player = Assassin("Player Assassin",1,90,11,7)
print("Вы выбрали:", player.__class__.__name__)
print("Противник:", enemy.__class__.__name__)

result = fight(player, enemy)

print(result)
