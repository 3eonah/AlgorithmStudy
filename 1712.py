# A 고정비용, B 가변비용, A + n*B = n개 생산비용 (총비용)
# 가격 * n = C (총수입) 
# 최초로 총수입 > 총비용 인 지점 = 손익분기점
# 손익분기점이 없을 땐 -1 출력
#A는 고정비용, B는 가변비용, C는 가격
A, B, C = map(int, input().split())

if B > C:
    # 손익분기점이 없을 때
    print(-1)
else:
    n=0     # 판매량 n
    while A + B*n >= C*n:
        n+=1 
    print(n)