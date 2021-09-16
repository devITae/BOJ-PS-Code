# 2775번: 부녀회장이 될테야

num=int(input())
for _ in range(num):
    arr=[]
    k=int(input())
    n=int(input())
    arr.append([i for i in range(1,n+1)])
    for i in range(1, k+1): # floor
        arr.append([])
        for r in range(n): # each room
            arr[i].append(sum(arr[i-1][0:r+1]))
    print(arr[k][n-1])