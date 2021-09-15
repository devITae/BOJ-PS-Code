n=int(input())
i,cnt,now=0,0,0
while cnt<n:
    i += 1
    cnt += i

if i%2==0: # 짝수줄 일 때
    y=i-(1+(n-(cnt-(i-1))))+1
    x=1+(n-(cnt-(i-1)))
else: # 홀수줄 일 때
    x=i-(1+(n-(cnt-(i-1))))+1
    y=1+(n-(cnt-(i-1)))
    
print(x,'/',y,sep='')