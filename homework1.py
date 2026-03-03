class Hero:
    def __init__(self,name,level,health,strength=10):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень:{self.level}')  
    
    def attack(self):
        print(f'{self.name} атакует!')
        self.strength -=1
        print(f'{self.name} использовал силу, текущая сила: {self.strength}')
        return 
    
    def rest(self):
        print(f'{self.name} отдыхает!')
        self.health +=1
        print(f'{self.name} восстановил здоровье, текущее здоровье: {self.health}')
        return

class Mage(Hero):
    def __init__(self,name,level,health,strength=10,mana=50):
        super().__init__(name,level,health,strength)
        self.mana = mana

    def cast_spell(self):
        print(f'{self.name} использует магию!')
        self.mana -= 5
        print(f'{self.name} использовал магию, текущая мана: {self.mana}')
        return


superman = Hero("clark kent", 100, 1000,100)
superman.greet()
superman.attack()
superman.rest()

batman = Hero("bruce wayne", 50, 500)
batman.greet()
batman.attack()
batman.rest()

gandalf = Mage("Gandalf", 100, 1000, 10, 200)
gandalf.greet()
gandalf.attack()
gandalf.rest()
gandalf.cast_spell()