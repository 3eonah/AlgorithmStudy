# 방 번호 N을 입력받음
N=int(input())

end_room=1
i=0
while True:
    if N==1:
        print(end_room)
        break
    else:
        i+=1
        end_room=end_room+6*i

        if N <=end_room:
            print(i+1)
            break