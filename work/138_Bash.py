n = int(input("Сумма - "))
den = [500,200,100,50,20,10]
q = 0
for a in den :
    while n - a >= 0 :
        n = n - a
        q = q + 1
if n != 0 :
    q = -1
print("Количество купюр -", q)