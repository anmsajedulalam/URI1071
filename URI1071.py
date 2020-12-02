x=int(input())
y=int(input())
max=int(0)
min=int(0)
sum=int(0)
if(x<y):
    max=y
    min=x
else:
    max=x
    min=y

for i in range(min+1, max):
    if(i%2==1 or i%2==-1):
        sum=sum+i

print(sum)