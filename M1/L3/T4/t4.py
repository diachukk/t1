'''
Виведіть площу виділеного червоним трикутника.

1) Запросіть два числа a і b - сторони прямокутника.
2) Зверніть увагу: площа червоного трикутника дорівнює половині площі намальованого прямокутника!
Відповідь має відповідати формату виведення, як вказано в прикладі. 
Формула знаходження площі  прямокутника S = a * b.
'''

a = int(input("Введіть першу сторону трикутника - ") )
b = int(input(" Введіть другу сторону трикутника - ") )
s = a * b /2
print("Площа трикутника =", s)
