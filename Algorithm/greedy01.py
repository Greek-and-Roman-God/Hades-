def coin(n):
 
 cnt=0

 coin_types=[500,100,50,10]
 for coin in coin_types:
   cnt += n // coin
   n%=coin



   print(cnt)


def rules():
 n,m,k=map(int,input().split()) #공백 구분 입력받기
 
 # n = 배열의 크기 , m = 숫자가 더해지는 수 
 # k = 연속해서 k 번을 초과할 수 없음
 
 x = list(map(int,input().split())) 
 
 x.sort() #입력받은 수 list로 정렬하기 S
 first = x[n-1] #가장 큰 수 
 second = x[n-2] #두 번째로 큰 수 

 result = 0

 while True:
   for i in range(k): #가장 큰 수를 k번 더하기
     if m ==0:
       break
     result += first
     m-= 1 # 더할때 마다 1을 빼기
   if m ==0:
    break #반복문 탈출
   result +=second
   m-= 1 #더할 때마다 1씩 빼기
 print(result)

def card_game():
  n,m =map(int,input().split())
  result=0
  for i in range(n):
   data=list(map(int,input().split()))
   min_num=min(data)
   result=max(result,min_num)
  
  print(result)

def goto_one():
  n,k=map(int,input().split())
  result= 0
  while n>=k:
    while n%k !=0 :
     n-=1
     result += 1

    n //=k #k로 나누기 
    result += 1
  
  while n>1:
   n-=1
   result +=1
  
  print(result)

def one():
  n,k=map(int,input().split())
  result=0
  # while True:
  #   value=(n//k)*k
  #   result+=(n-value)
  #   n=value
  #   if n<k:
  #     break;

  # result +=1
  # n//=k
    
  while n>1:
    result+=n%k
    n-=n%k
    n/=k
    result+=1
    
  print(result)

