def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)
def lcm(a, b):
  return a // gcd(a, b) * b

res = 1
for i in range(1, 21):
  res = lcm(res, i)
print(res)