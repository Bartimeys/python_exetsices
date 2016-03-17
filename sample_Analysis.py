# Описание задачи
# Часто требуется проанализировать какой-то ряд
#  значений и определить количество значений,
#  попавших в каждый определенный диапазон.
# Например, дан список, содержащий 1000 значений
# натуральных чисел в диапазоне от 1 до 100.
# Требуется подсчитать, сколько значений попало
#  в диапазоны от 1 до 20, от 21 до 30, от 31 до 40 и т.д.
# Полученный таким образом результат можно использовать для построения графиков
# и диаграмм частот встречаемости значений.



# Analyte list (you can substitute another)
a = [3, 5, 7, 3, 8, 1, 8, 0, 7, 3, 2, 4, 6, 8, 5, 4, 3, 3, 6, 5, 7, 8, 9, 5, 3, 2, 3]

bottom = int(input("lower boundary: "))
top = int(input("upper bound: "))
interval = int(input("Interval: "))

# Number of intervals
num_interval = int((top - bottom) / interval)
  
top = bottom
for i in range(num_interval):
    bottom = top
    top = top + interval
    print("From", bottom, "to", top)
    calculator = 0
    for j in a:
        if bottom <= j < top:
            calculator += 1
        print(calculator,"values\n")
