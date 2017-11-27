import json

with open('xy_coord.txt', 'r') as f:  # извлекаем  из файла
    data2 = json.load(f)
    
data_fin2 = []
i = 0
for item in data2:  # приводим к типу Python
    data_fin2.append(list(item))

print('список координат x y', data_fin2)  # проверка готового результата
# все первые индексы отражают имя координаты
print(data_fin2[0][0])
print(data_fin2[1][0])
print(data_fin2[2][0])
# все следущие индексы выдают список  координат
print(data_fin2[0][1]) #[291, 207]
print(data_fin2[1][1]) #[163, 195]
print(data_fin2[2][1]) #[242, 252]
# следущий третий индекс выдает по отдельности x и y  координат
print(data_fin2[0][1][0]) # x=291
print(data_fin2[1][1][0]) # x=163
print(data_fin2[2][1][1]) # y=252