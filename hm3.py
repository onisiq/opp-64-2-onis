class Money:
    rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}
#create a атрибуты
    def __init__(self,amount,currency):
        self.amount =amount
        self.currency = currency
    """подсчет денег через словарь"""
#добавил методы конвертации
    def conver_to_kgs(self,):
        return self.amount *Money.rates[self.currency]

#used add 
    def __add__(self,other):
        total_kgs = self.conver_to_kgs() + other.conver_to_kgs()
        return Money(total_kgs,"KGS")
#used sub
    def __sub__(self,other):
        total_kgs = self.conver_to_kgs() - other.conver_to_kgs()
        return Money(total_kgs,"KGS")
#used mul
    def __mul__(self,number):
        return Money(self.conver_to_kgs()  * number, self.currency)
#used truediv
    def __truediv__(self,number):
        return  Money(self.conver_to_kgs()  / number, self.currency)
#used str to write text
    def __str__(self):
        return f"{self.amount}, {self.currency}"




#checking 
money1 = Money(100, "USD")
money2 = Money(2000, "KGS")

print(money1 + money2)  # сложение
print(money1 - money2)  # вычитание
print(money1 * 3)       # умножение
print(money1 / 2)       # деление
print(money1) 