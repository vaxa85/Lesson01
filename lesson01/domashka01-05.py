revenue = int(input("Введите сумму прибыли >>> "))
expenses = int(input("Введите сумму трат >>> "))
if revenue > expenses:
    print(f"Рентабельность {revenue / expenses:.2f}")
    staff = int(input("Введите количество персонала >>> "))
    print(f"Прыбиль с сотрудника {revenue / staff:.2f}")
elif revenue == expenses:
    print("Рентабильность ноль")
else:
    print("Фирма не рентабильна")