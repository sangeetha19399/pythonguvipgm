a1=int(input())
arr=list(map(int,input().split()))
for i in range(a1-1):
    if(arr[i]>arr[i+1]):
        print(i)
