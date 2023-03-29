# (세 자리 수) * (세 자리 수) 과정에 들어갈 값 구하기
# 입력: 첫째줄에 곱할 세자리 자연수a, 둘째줄에 곱할 세자리 자연수b
# 출력: 
#   첫째줄: 자연수a와 자연수b의 1의 자리수와 곱한 값
#   둘째줄: 자연수a와 자연수b의 10의 자리수와 곱한 값
#   셋째줄: 자연수a와 자연수b의 100의 자리수와 곱한 값
#   넷째줄: 자연수a와 자연수b의 곱의 최종값

# 첫째, 둘째줄에 수를 입력받음
a=int(input())
b=int(input())

# 입력받은 자연수가 세 자리 수일 때
if (99<a<1000) and (99<b<1000):
    
    #자연수 b를 str으로 바꾸고
    b_str = str(b)
    #이를 또 list로 변환 Ex) "123" -> ['1','2','3']
    b_list=list(b_str)
    #list역순으로 바꾸고 리스트의 값 자연수로 바꾸기
    reserved_b_list=list(reversed(b_list))
    b_nums=[]
    for i in range(len(reserved_b_list)):
        b_nums.append(int(reserved_b_list[i]))

    #자연수a와 자연수b 1,10,100의 자리수의 곱 m1, m2, m3
    m1=a*b_nums[0]
    m2=a*b_nums[1]
    m3=a*b_nums[2]
    #자연수a와 자연수b의 곱 m4
    m4 = m1 + m2*10 + m3*100

    print(m1)
    print(m2)
    print(m3)
    print(m4)







