import random


print('Введите число от 1 до 10')
numb = int(input())

guess = random.randrange(1,11)

n = 0

while numb != guess:
    guess = random.randrange(1,11)
    print(numb,'==',guess)
    if guess == numb:
      print('Получилось!!!')
    else:
      print('Не получилось:(((')
    n += 1
print('Количество попток:', n)
test