def map():
 N = int(input())
 command = input().split()

 X,Y= 1,1
 direction = ['R','L','U','D']

 for command in direction:
   X,Y <= N
   if 'R' in command :
     Y+= 1
   if 'L' in command :
     if Y>0:
       Y+= 1




 print(X,Y)


def time():
  h = int(input())

  cnt = 0
  for i in range(h+1):
    for j in range(60):
      for k in range(60):
        if '3' in str(i) + str(j) + str(k):
          cnt += 1

  print(cnt)

