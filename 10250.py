# 10250번: ACM 호텔
num=int(input())
for _ in range(num):
    cnt=0
    h,w,n=map(int,input().split())
    arr=[[0 for _ in range(w)] for _ in range(h)]
    for i in range(w):
        for j in range(h):
            cnt += 1
            if arr[j][i] == 0:
                if cnt == n:
                    print(j+1,str(i+1).zfill(2),sep='')
                    break
                else:
                    arr[j][i] = 1