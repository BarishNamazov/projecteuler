n, i, res = 600851475143, 2, 0
while i * i <= n:
  if n % i == 0:
    res = i
    while n % i == 0:
      n //= i
  i += 1
if n > 1:
  res = n
print(res)