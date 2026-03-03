class Hero:
    #конструктор класса
    def __init__(self,name,lvl,hp):
        #атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        print(f'{self.name} атакует!')
    def __str__(self):
        return self.name
    
class MagicHero(Hero):
    pass
hero1 = Hero('Герой1', 1, 100)
print(hero1)
hero1.action()

gendolf = MagicHero('Гендольф', 100, 1000)
print(gendolf)
gendolf.action()        