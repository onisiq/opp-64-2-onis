from abc import ABC, abstractmethod

class Hero:
    def __init__(self,name,lvl,hp):
        self.name=name
        self.lvl=lvl
        self.hp=hp
    
    def action(self):
        print(f'{self.name} готов к бою!')
    
class MageHero(Hero):
    def __init__(self, name, lvl, hp,mp):
        super().__init__(name, lvl, hp)
        self.mp=mp

    def action(self):
        print(f'Маг {self.name} кастует магию! MP: {self.mp}')

class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp):
        self.name=name
        self.lvl=lvl
        self.hp=hp

    def action(self):
        print(f'Воин {self.name} Рубит мечом lvl: {self.lvl}')

class BankAccount:
    bank_name = 'Hero Bank'
    def __init__(self,hero,balance,password):
        self.hero=hero
        self._balance=balance
        self.__password=password
    
    def login(self,password):
        if password ==  self.__password:
            print('Login successful')
            return True
        else:
            print('error')
            return False
    
    @property
    def full_info(self):
        return f"Hero: {self.hero.name}, Balance: {self._balance}"

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            print('герои должны быть одного класса')
    
    def __eq__(self, other):
        return (self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl)


class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass
    
class KGSms(SmsService):
    def send_otp(self, phone):
        return f'<text>Код: 1234</text><phone>{phone}</phone>'

class RUSms(SmsService):
    def send_otp(self, phone):
        return {
            'text': "Код: 1234",
            'phone': phone
        }

        


mage1 = MageHero('Merlin', 80, 500, 150)
mage2 = MageHero('Merlin', 80, 500, 200)
warrior = WarriorHero('Leon', 52, 222)

acc1 = BankAccount(mage1, 5000, "1234")
acc2 = BankAccount(mage2, 3000, "0000")
acc3 = BankAccount(warrior, 2500, "1111")


mage1.action()
warrior.action()

print(acc1)
print(acc2)

print('Банк:', acc1.get_bank_name())
print('Бонус за уровень:', acc1.bonus_for_level(), 'SOM')


print('\n=== Проверка __add__ ===')
print('Сумма счетов двух магов:', acc1 + acc2)

print('Сумма мага и воина:', acc1 + acc3)


print('\n=== Проверка __eq__ ===')
print('Mage1 == Mage2?', acc1 == acc2)
print('Mage1 == Warrior?', acc1 == acc3)


sms = KGSms()
print('\n', sms.send_otp('+996777123456'))


    