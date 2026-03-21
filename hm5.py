from faker import Faker

#Faker — это очень крутая библиотека для генерации фейковых (выдуманных) данных.
#check
fake = Faker()

print('random name:', fake.name())
print('random adress :', fake.address())
print('random email:', fake.email())


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 18

print(two_sum(nums, target))