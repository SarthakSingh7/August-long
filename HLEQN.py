T = int(input())
for i in range(T):
    x = int(input())
    flag = 0
    for i in range(1,x+1):
        if i*i > x:    # the step decreses the number of computations
            break   # if i*i is greater than x then the loop will break
        if (x - 2*i)%(i+2) == 0 and x != 2*i:
            print('YES')
            flag = 1
            break
    if flag == 0:
        print('NO')
        
    # treat i as a 
    # 2a + 2b + ab = x
    # 2b + ab = x - 2a
    # b(a + 2) = (x-2a)
    # b = (x - 2a)/ (a+2)
    # for the equation to satisfy 
    # b should be equal to 1 
    # that means (x - 2a) % (a + 2) == 0
    # put a = i 
    # (x - 2*i) % (i + 2) == 0
    # this step decreases the computations
