def party():
  
  total=list(map(int,input().split()))
  total.sort() #정렬
  result=0 #총 그룹의 수
  cnt = 0 #모험가의 수 

  for i in total:
    #i 는 공포도
    cnt+=1 #제일 낮은 공포도 부터 그룹에 넣기
    if cnt>=i: #그룹에 넣는게 공포도 보다 많아지면 
      result +=1 #그룹 추가
      cnt=0 # 길드원 초기화 
  
  print(result)


def multiple() : 
  data = input()
  result = int(data[0])

  for i in range(1,len(data)):
    num=int(data[i])
    if num <= 1 or result<= 1:
      result+=num
    else:
      result *= num

  print(result)


