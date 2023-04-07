# 재귀함수 메모리제이션과 조기리턴 활용
Memo={0:0, 1:1}
def Fibo(n):
    if n in Memo:   # 조기리턴
        return Memo[n]
    output = Fibo(n-1)+Fibo(n-2)
    Memo[n]=output
    return output

N=int(input())
print(Fibo(N))