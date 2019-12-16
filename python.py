n = int(input())
row = []
col = []
for i in range(n):
   row.append(int(input()))
   col.append(int(input()))
def fR(k): 
    for i in range(n): 
        if k==row[i]: 
         return 0 
    return 1 
def fC(k):
    for i in range(n): 
         if k==col[i]: 
             return 0 
    return 1 
ans = 0 
for i in range(0,8): 
    for j in range(0,8): 
        if fR(i) and fC(j): 
            ans+=1 
print(ans)