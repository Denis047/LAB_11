"""
 Завдання №1:
 TODO: метод безпосереднього оцінювання
 Варіант - №2
*------------------------------*
# |   xij      | Експерт 1 | Експерт 2 | Експерт 3 |
# |-----------|-----------|-----------|-----------|
# | Захід 1   | 0         | 0.4       | 0.5       |
# | Захід 2   | 0         | 0.3       | 0         |
# | Захід 3   | 0.3       | 0.1       | 0.2       |
*------------------------------*

"""
array = [
    [0, 0.4, 0.5],
    [0.0, 0.3, 0],
    [0.3, 0.1, 0.2]
]

rationing_factor = 0
means = []

for expert_row in array:
    mean = round(sum(expert_row), 1) / 3
    means.append(mean)
    summ = round(sum(expert_row), 1)
    rationing_factor += mean * summ

columns = []

for i in range(3):
    for j in range(3):
        columns.append(array[j][i])

k_1 = sum(columns[:3]) * means[0] / rationing_factor
k_2 = sum(columns[3:6]) * means[1] / rationing_factor
k_3 = sum(columns[6:]) * means[2] / rationing_factor

print('\nФактор нормування:', rationing_factor)
print("\nФактори компетентності:")
print(k_1)
print(k_2)
print(k_3)
