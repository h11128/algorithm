A = "10010101"
B = "010110110"
#Find the longest common subsequence, doesn't have to be contiguous

a = len(A)
b = len(B)
L = {}
S = {}

def LCS(m,n):
    if m == 0 or n ==0:
        L[m,n] = 0
        S[m,n] = ""
        return L[m,n]
    if A[m-1] == B[n-1]:
        L[m,n] = L[m-1,n-1] + 1
        S[m,n] = S[m-1,n-1] + A[m-1]
    elif L[m-1,n] > L[m,n-1]:
        L[m,n] = L[m-1,n]
        S[m,n] = S[m-1,n]
    else:
        L[m,n] = L[m,n-1]
        S[m,n] = S[m,n-1]


for i in range(0,a+1):
    for j in range(0,b+1):
        LCS(i,j)
for i in L:
    print(i," num: ",L[i]," string: ",S[i])
