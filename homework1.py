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
        return self.strength
    
    def rest(self):
        print(f'{self.name} отдыхает!')
        self.health +=1
        print(f'{self.name} восстановил здоровье, текущее здоровье: {self.health}')
        return

superman = Hero("clark kent", 100, 1000,100)
superman.greet()
superman.attack()
superman.rest()

batman = Hero("bruce wayne", 50, 500)
batman.greet()
batman.attack()
batman.rest()

        