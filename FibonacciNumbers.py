import time


def Fibonacci(n):
    F = [0,1]
    start_time = time.clock()
    if n <= 1:
        return F[n]
    while len(F) < n+1:
        F.append(F[-1]+F[-2])

    #print(F[n])
    print("--- %s seconds ---" % (time.clock() - start_time))

def Fibonacci1(n):
    start_time = time.clock()
    F = [-1] *(n+1)
    F[0] = 0
    F[1] = 1
    F[n] = recursive(F,n)
    #print(F[n])
    print("--- %s seconds ---" % (time.clock() - start_time))

def recursive(F,n):
    if n ==1 or n ==0:
        return F[n]
    if F[n] >0:
        return F[n]
    else:
        F[n] = recursive(F,n-1) + recursive(F,n-2)
        return F[n]

def Fibonacci2(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return Fibonacci2(n-1) + Fibonacci2(n-2)

def Fibonacci3(F,n):


    while len(F) < n + 1:
        F.append(-1)

    if n <=1:
        return F[n]
    else:
        if F[n-1] < 0:
            F[n-1] = Fibonacci3(F,n-1)
        if F[n-2] < 0:
            F[n-2] = Fibonacci3(F,n-2)
        F[n] = F[n-1] + F[n-2]
    return F[n]

def fib(f,n):
    if n == 0:
        return 0
    if n == 1 or n ==2 :
        f[n] = 1
        return f[n]
    if(f[n]):
        return f[n]

    if( n & 1) :
        k = (n + 1) // 2
    else :
        k = n // 2

    if((n & 1) ) :
        f[n] = (fib(f,k) * fib(f,k) + fib(f,k-1) * fib(f,k-1))
    else :
        f[n] = (2*fib(f,k-1) + fib(f,k))*fib(f,k)

    return f[n]

def Fibonacci4(n):

    start_time = time.clock()
    f = [0] * (n+1)
    fib(f,n)
    #print(f[n])
    print("--- %s seconds ---" % (time.clock() - start_time))

Fibonacci(150000)

Fibonacci4(150000)
