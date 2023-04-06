def Fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>=2:
        return Fibo(n-1)+Fibo(n-2)

N=int(input())

if 0<=N<=90:
    print (Fibo(N))