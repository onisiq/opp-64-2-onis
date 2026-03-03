# class Hero:
#
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def action(self):
#         return f"{self.name} Base action"
#
# class MageHero(Hero):
#
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     def action(self):
#         return f"HP: {self.hp} NAME: {self.name}"
#
#     def cast_spell(self):
#         return f"{self.mp} cast spell {self.name}"
#
# kirito = Hero("Kirito", 100, 1000)
# asuna = MageHero("Asuna", 1000, 1000, 99)
#
# print(kirito.name)
# print(asuna.name)



class Step:
    def action(self):
        print('Step')

class Fly:
    def action(self):
        print('Fly')

class Swim:
    def action(self):
        print('Swim')

class Animal(Fly, Step, Swim):
    ...

duck = Animal()
# duck.action()
# print(Animal.mro())



class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print("B")
class C(A):
    def action(self):
        super().action()
        print("C")
class D(B, C):
    def action(self):
        super().action()
        print("D")

test = D()
# test.action()
# print(D.mro())