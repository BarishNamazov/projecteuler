N = 200000
cnt = 0
prime = [1] * N
for i in range(2, N):
  if prime[i]:
    cnt += 1
    if cnt == 10001:
      print(i)
      break
    for j in range(i * i, N, i):
      prime[j] = 0