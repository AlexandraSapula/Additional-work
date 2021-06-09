m = int(input("горизонтальная сторона  = "))
n = int(input("вертикальная сторона = "))
x = 0
y = 0
dx = 1
dy = 1
k = 0
d = 0
while True :
    if dx == 1 :
        tx = m-x
    else :
        tx = x
    if dy == 1 :
        ty = n-y
    else :
        ty = y 
    
    t = min(tx,ty)
    y = y + t*dy
    x = x + t*dx
    if tx < ty :
        print ("ударится о вертикальную сторону ")
        dx = dx*-1 
    elif tx > ty :
        print ("ударится о горизонтальную сторону ")
        dy = dy *-1
    else :
        print("попали в лузу")
        if x==0 and y==0 :
            d = 1
        elif x==m and y==0 :
            d = 2
        elif x==m and y==n :
            d = 3
        elif x==m and y==0 :
            d = 4
        break
    k = k + 1 
print ("ударов = ", k )
print ("луза = " ,d)