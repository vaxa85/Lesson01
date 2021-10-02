a = int(input("Введите дистанцию пробежки в километрах первого дня >>> "))
b = int(input("Введите нужную дистанцию в километрах >>> "))
distance_km_first_day = 1
total_distance_km = a
while total_distance_km < b:
    a = a + 0.1 * a
    distance_km_first_day += 1
    total_distance_km = total_distance_km + a
print(f"За %.d дня будет достигнут результат" % distance_km_first_day)
