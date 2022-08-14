for i in range(int(input())):
    N = int(input())
    n = input().split()
    l = []
    s = 0
    for i in n:
        l.append(int(i))
    s = s + 2*max(l)
    l.remove(max(l))
    for i in range(len(l)):
        s = s + l[i]
    print(s)
    
# logic 
# add the maximum numbers from the array twice
# add the rest of numbers
# logic derived from testcases
# eg: array 3 5
# answer = 5 + 3 + 5
# eg: array 5 2 6
# answer = 6 + 5 + 2 + 6
