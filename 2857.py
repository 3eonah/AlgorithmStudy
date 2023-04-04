# 입력
# 5개 줄에 요원의 첩보원명이 주어진다. 첩보원명은 알파벳 대문자, 숫자 0~9, 대시 (-)로만 이루어져 있으며, 최대 10글자이다.
# 출력
# 첫째 줄에 FBI 요원을 출력한다. 
# 이때, 해당하는 요원이 몇 번째 입력인지를 공백으로 구분하여 출력해야 하며, 오름차순으로 출력해야 한다. 만약 FBI 요원이 없다면 "HE GOT AWAY!"를 출력한다.

agents=[]
for i in range(5):
    a=input()
    agents.append(a)

fbi=[i+1 for i in range(len(agents)) if "FBI" in agents[i]]

if len(fbi) != 0:
    for i in range(len(fbi)):
        print(fbi[i], end=' ')
else:
    print("HE GOT AWAY!")

    

