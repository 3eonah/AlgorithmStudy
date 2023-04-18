# 그룹단어 체커
# 각 문자가 연속해서 나타나는 그룹단어의 개수 출력
# ccazzzzbb -> 그룹단어
# aabbba -> 그룹단어 x


N=int(input())
count=N     # 그룹단어의 개수 count

for i in range(N):
    str=input()
    breaker=False       # 2중 for문을 멈추기 위한 breaker

    for j in range(len(str)-1):
        if breaker==True:
            break

        elif str[j]==str[j+1]:
            continue
        
        else:
            for k in range(j+2, len(str)):
                if str[j]==str[k]:
                    count-=1
        
                    breaker=True
                    break

print(count)


    

    


