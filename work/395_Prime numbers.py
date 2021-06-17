def simple(n, mas) :
    for ch in mas :
        if ch != n and n % ch == 0  :
            return False
    return True
n = int(input("Количество чисел = "))
a = str(input("Числа - "))
s = a.split(" ")
print(s)
w = []
for ch in s :
    w.append(int(ch))
print(w)
v = []
for ch in w :
    if simple(ch,w) :
        v.append(ch)
print(v)