# Armstrong Number

n=int(input())
temp = n
new_num = 0
while temp>0:
    digit = temp%10
    new_num = new_num + digit**3
    temp = temp//10
if new_num == n:
    print('true')
else: 
    print('false')
