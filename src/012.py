def divcnt(x):
  i, cnt = 1, 0
  while i * i <= x:
    if x % i == 0:
      cnt += 1 + (x // i != i)
    i += 1
  return cnt

i = 1
while True:
  if divcnt(i * (i + 1) // 2) > 500:
    print(i * (i + 1) // 2)
    break
  i += 1