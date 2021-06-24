def circle(p1,p2,r) :
    p = [0.0,0.0]
    while True :
        p[0] = (p1[0] + p2[0])/2.0
        p[1] = (p1[1] + p2[1])/2.0
        if p[0]**2 + p[1]**2 < r**2 :
           p1[0] = p[0]
           p1[1] = p[1]
        else :
           p2[0] = p[0]
           p2[1] = p[1]
        if abs(p2[0] - p1[0] )< 0.001 and abs(p2[1] - p1[1] )< 0.001 :
            return p
r = float(input("Радиус = "))
if r <=0 :
    print("Error")
    exit()
h = float(input("Шаг = "))
if r < h :
    print("Длина равна - ", r)
    exit()
r = r *100
k = h
x = 0
y = 0
len = 0
mas = ["T","R","B","L"]

while True :
    for ch in mas :
        x = y 
        if ch == "T" :
            len = len + h
            y = y + h

        elif ch == "R" : 
            len = len + h
            h = h + k

        elif ch == "B" :
            len = len + h
            y = y - h

        elif ch == "L" :
            len = len + h
            h = h + k
        if x**2 + y**2 > r**2 :
            if x < 0 :
                p = circle([x,y-k],[x,y],r)
                w = y - p[1] 
            else :
                p = circle([x-k ,y],[x,y],r)
                w  = x - p[0]
            print ("Длина равна -",round((len - w)/100,3)," ",(len-w)/100)
            exit()