for i in range(int(input())):
    x = int(input())
    dis = 0
    if x <= 100:
        dis = 0
    elif 100<x<= 1000:
        dis = 25  # rupees 
    elif 1000 < x <= 5000:
        dis = 100
    elif x > 5000:
        dis = 500
    final = x - dis
    print(final)
