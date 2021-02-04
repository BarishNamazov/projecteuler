N = 2000000
res = 0
prime = [1] * N
for i in range(2, N):
  if prime[i]:
    res += i
    for j in range(i * i, N, i):
      prime[j] = 0
print(res)