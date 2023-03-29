#인공지능 오븐이 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산
#오븐 앞면엔 사용자에게 요리가 끝나는 시각을 알려주는 디지털 시게가 있음
#입력: 요리를 시작하는 시각(A시 B분), 오븐구이를 하는 데 필요한 시간이 분 단위로 주어짐
# 0<=A<=23, 0<=B<=59
#디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다
#출력: 오븐구이가 끝나는 시간을 출력(A B)

# 현재 시간 A, 현재 분 B
A, B=map(int, input().split())
# 요리 소요 시간 C
C=int(input())

# 시간, 분, 요리 소요시간 범위 제한
if (0<=A<=23) and (0<=B<=59) and (0<=C<=1000):

    add_h=C//60  # 현재 시간에 추가할 시간
    add_m=C-(60*add_h) #현재 분에 추가할 분

    # 요리 끝날 시간 end_h, 분 end_m
    end_h=A+add_h
    end_m=B+add_m

    # 59보다 큰 양 만큼 시간에 추가
    if end_m > 59:
        extra_h = end_m//60
        end_h += extra_h
        end_m = end_m - (60*extra_h)

#종료시간이 24시 60분이라고 칠 때
# -> 25시(24+1) 0분 (60-60)

if (end_h > 23):
    end_h-=24
print(end_h, end_m)




    

        


    
    
