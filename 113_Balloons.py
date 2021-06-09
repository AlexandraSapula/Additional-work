print ("Цвета шариков:1 - синий, 2 - зеленый, 3 - голубой, 4 - красный, 5 - розовый, 6 - желтый, 7 - серый, 8 - черный, 9 - белый")
color_min = 1
color_max = 9
n = int(input("Колическтво шариков = "))
mas = []
for m in range(n) :
    c = int(input("Цвет шаров - "))
    if c > color_max or c < color_min :
        exit()
    mas.append(c)
#print(mas)
counts = []
for i in range(color_min, color_max+1):
    counts.append(0)

for color in mas :
    counts[color-1] = counts[color-1]+1
#print(counts)
print("перекрасить нужно -", n - max(counts))