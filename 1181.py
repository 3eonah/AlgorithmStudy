# N개의 단어 정렬
# 단어 길이 순, 길이가 같을 땐 사전순
# 중복 단어 X


n=int(input())  # 입력 받을 단어의 개수 n
words={}    
for i in range(n):
    key=input()
    val=len(key)
    # 딕셔너리 words의 vkey는 입력받은 단어, val는 단어의 길이
    # key값은 중복될 수 없으므로 중복 입력된 단어는 자동으로 사라짐
    words[key]=val      
    
# 딕셔너리 value값을 기준(단어길이)으로 오름차순으로 정렬한 후, key값(알파벳)을 기준으로 오름차순
words=sorted(words.items(), key=lambda x:(x[1],x[0]))
words=dict(words)

for key in words.keys():
    print(key)












    
    
