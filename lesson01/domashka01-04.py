a = abs(int(input("Введите число >>> ")))
max_number = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > max_number:
        max_number = a % 10
    if a > 9:
        continue
    else:
        print(max_number)
        break
