class Hero:
    def __init__(self,name,level,health,strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    
    def great(self):
        print(f'Привет, я {self.name}, мой уровень:{self.level}')
    
    def attack(self):
        print(f'{self.name} Атакует!')

    def rest(self):
        print(f'{self.name} Отдыхает!')
        self.health += 1
        print(f'{self.name} здоровье увеличилось до {self.health} ') 
        return
    
class Warrior(Hero):
    def __init__(self, name, level, health, strength,stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f'{self.name} атакует мечом!')
        self.stamina -= 1
        print(f'{self.name} герой устал {self.stamina}')
        return
    
class Mage(Hero):
    def __init__(self, name, level, health, strength,mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    
    def attack(self):
        print(f'{self.name} использует магию!')
        self.mana -= 1
        print(f'{self.name} герой потратил {self.mana}')
        return

class Assassin(Hero):
    def __init__ (self,name,level,health,strength,stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    
    def attack(self):
        print(f'{self.name} использует скрытность!')
        self.stealth -= 1
        print(f'{self.name} герой потратил {self.stealth}')
        return

Kratos = Warrior("Kratps",100,1000,100,50)
Kratos.great()
Kratos.attack()
Kratos.rest()

Harry_Potter = Mage("Harry Potter", 80, 800, 80, 200)
Harry_Potter.great()
Harry_Potter.attack()
Harry_Potter.rest()

agent_007 = Assassin("Agent 007", 90, 900, 90, 70)
agent_007.great()
agent_007.attack()
agent_007.rest()
    
