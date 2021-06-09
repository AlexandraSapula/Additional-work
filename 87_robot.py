def max(a,b) :
    if a < b :
        return b 
    else :
        return a
def min(a,b) :
    if a > b :
        return b 
    else :
        return a 
m = str(input("Ввод - "))
k = 0 
k_max = 0
k_min = 0
for ch in m :
    if ch == 'R' :
        k = k + 1 
    elif ch == 'L' :
        k = k - 1 
    else :
        pass
    k_max = max(k_max,k)
    k_min = min(k_min,k)

print ("Колическво клеток = ", k_max + 1 - k_min)