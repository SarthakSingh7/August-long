for i in range(int(input())):
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    A = max(a,b)
    B = min(a,b)
    p = int(A/B)
    out = ''
    while A>= b:
        if a == b:
            out = 'YES'
        for i in range(1,p+1):
            m = B*2**i
            if m == A: 
                out = 'YES'
                break
        break
    if out == 'YES':
        print(out)
    else:
        print('NO')
