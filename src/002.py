a, b, res = 1, 2, 0
while b < 4000001:
  res += b * (b % 2 == 0)
  a, b = b, a + b
print(res)