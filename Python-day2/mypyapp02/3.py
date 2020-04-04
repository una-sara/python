#while
#求1+2+3+...+100

"""
i = 0
sum = 0
while( i<=100 ):
  sum += i
  i += 1
"""

sum = 0
for  n   in  range(0,101,1):
  #print(n)
  sum += n

print('1~100的累加和为：',  sum)
