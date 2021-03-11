size=int(input())
max=0
count=0
flag=0
str=input()
arr=list(str)

for i in range(0,size):
    if arr[i]=='1':
        count=count+1;
        flag=1;
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)