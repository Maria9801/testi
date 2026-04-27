number = input("Введите номер карты ")
while len(number) != 4:
  print("Неверный номер")
  number = input("Введите номер карты ")
discount = 0
count = 0
while count < 4:
  discount += int(number[count])
  count += 1
print(discount, "%")