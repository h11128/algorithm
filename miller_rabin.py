
def miller(n):
    if n % 2 == 0:
        print("composite")
    u = n-1
    t = 0
    while(u % 2 == 0):
        t = t + 1
        u = u / 2
    a = P(3,u,n,t)
    print(end="\n")
    b = P(5,u,n,t)
    print(end="\n")
    c = P(7,u,n,t)
    if(a and b and c):
        print(end="\n")
        print("prime")



def P(a,u,n,t):
    num = a**u % n
    print(num,end=" ")
    if num == 1:
        return True

    for i in range(t):
        num = (num*num) % n
        print(num,end=" ")
        if num == n-1:
            return True

    return False

miller(777)
