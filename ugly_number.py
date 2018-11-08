import time

"""
ugly number: number that the prime factors are 2,3,5
super ugly number: given primes list
allugly1 : return nth ugly number by check number one by one, if it is ugly the
    counter create 1 until count reach n.
allugly2 : calculate ugly number by the number already have multiply the prime
    factor, up and up until the nth number. Notice that the repeat multiply
    result should count only once, for example: 2*3 = 3*2
allugly3: try to use set to solve this prolelm, by mutilply the set with 2,3,5
    until the number of the set bigger than n. But will miss some number because
    2 and 3 should have mutilply more time than 5. Now I don't find ways to solve it.
superugly: give a prime list and find the nth ugly number. The same as allugly2
    except this time there is a prime list and candidate list.

"""
def allugly1(n):
    start_time = time.clock()
    count = 0
    i = 0
    while (count != n):
        i = i + 1
        if ugly(i):
            count += 1
    print("%dth ugly number is %d"%(n,i))
    print("--- %s seconds ---" % (time.clock() - start_time))

def ugly(i):
    while (i % 2 == 0):
        i = i / 2
    while (i % 3 == 0):
        i = i / 3
    while (i % 5 == 0):
        i = i / 5
    if i == 1:
        return True
    else: return False

def allugly2(n):
    start_time = time.clock()
    ugly = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    for i in range(1,n):
        c = min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5)
        ugly.append(c)
        if ugly[i] == ugly[i2]*2:
            i2 += 1
        if ugly[i] == ugly[i3]*3:
            i3 += 1
        if ugly[i] == ugly[i5]*5:
            i5 += 1
    #return(ugly[1800:1899])
    print(i2-i5)
    #print("%dth ugly number is %d"%(n,ugly[n-1]))
    #print("--- %s seconds ---" % (time.clock() - start_time))

def allugly3(n):
    start_time = time.clock()
    ugly = set([1])
    i = -1
    while(len(ugly)<n//3):
        uglyi2 = set([v*2 for i,v in enumerate(ugly)])
        uglyi3 = set([v*3 for i,v in enumerate(ugly)])
        uglyi5 = set([v*5 for i,v in enumerate(ugly)])
        ugly = ugly.union(uglyi2,uglyi3,uglyi5)
        i = i+1
    c = max(ugly)

    while(2**i <c and 3**i<c):
        uglyi2 = set([v*2 for i,v in enumerate(ugly)])
        uglyi3 = set([v*3 for i,v in enumerate(ugly)])
        ugly = ugly.union(uglyi2,uglyi3)
        i = i+1
    ugly = list(ugly)
    ugly.sort()
    #return(ugly[1800:1899])
    print("%dth ugly number is %d"%(n,ugly[n-1]))
    print("--- %s seconds ---" % (time.clock() - start_time))
    print(len(ugly))

def superugly(primes,n):
    start_time = time.clock()
    iprimes = [0]  * len(primes)
    cc = primes.copy()
    ugly = [1] * n
    for i in range(1,n):
        c = min(cc)
        ugly[i] = c
        for j in range(len(primes)):
                if c == cc[j]:
                    iprimes[j] += 1
                    cc[j] = ugly[iprimes[j]] * primes[j]
    print("%dth ugly number is %d"%(n,ugly[n-1]))
    print("--- %s seconds ---" % (time.clock() - start_time))

def num_of_ugly(n):
    start_time = time.clock()
    ugly = [1]
    i = 0
    i2 = 0
    i3 = 0
    i5 = 0
    while ugly[-1] < n:
        i = i +1
        c = min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5)
        ugly.append(c)
        if ugly[i] == ugly[i2]*2:
            i2 += 1
        if ugly[i] == ugly[i3]*3:
            i3 += 1
        if ugly[i] == ugly[i5]*5:
            i5 += 1

    print("# of ugly number in range(%d) is %d"%(n,i+1))
    print("--- %s seconds ---" % (time.clock() - start_time))



superugly([2,3,5],9)
num_of_ugly(3000000000)
b = allugly3(1900)
