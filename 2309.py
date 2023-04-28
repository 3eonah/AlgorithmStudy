# 일곱 난쟁이
# 100 이하의 자연수 9개를 9개의 줄에 걸쳐 입력받음
# 9개의 수는 모두 다름
# 7개 자연수의 합이 100인 경우, 오름차순으로 7개의 수를 출력
# 정답이 여러가지인 경우 아무거나 출력 (정답이 없는 경우는 없음)

dwarfs=[]
for i in range(9):
    n=int(input())
    dwarfs.append(n)

s=0
real=[]

for i in range(len(dwarfs)):
    if s<100:
        s+=dwarfs[i]
        real.append(dwarfs[i])
    elif s>100:
        i-=1
        s-=dwarfs[i]
        del real[i]
    else:
        break

print(s)
print(real)




