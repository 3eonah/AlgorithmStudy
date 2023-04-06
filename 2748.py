# 재귀함수 이용 -> 시간초과
# def Fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     elif n>=2:
#         return Fibo(n-1)+Fibo(n-2)

# N=int(input())

# if 0<=N<=90:
#     print (Fibo(N))
#--------------------------

# 리스트 이용
n=int(input())

if 0<=n<=90:
    Fibo=[]
    for i in range(n+1):
        if i==0:
            Fibo.append(0)
        elif i==1:
            Fibo.append(1)
        else:
            Fibo.append(Fibo[i-2]+Fibo[i-1])
    print(Fibo[n])
