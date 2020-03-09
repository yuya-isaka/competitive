def is_ok(k):
  C = sorted([(k - h[i])/s[i] for i in range(n)])  
  for i in range(n):
    if C[i]<0 or C[i]< i:
      return False
  return True
 
n = int(input())
h = [0]*n
s = [0]*n
for i in range(n):
  h[i],s[i] = map(int,input().split())
 
l = 0
r = 10**14
while l<r:
  m = (l+r)//2
  if is_ok(m):
    r = m
  else:
    l = m+1    
    
print(r) 