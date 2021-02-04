memo = {1: 1}
def collatz(n):
  if n in memo:
    return memo[n]
  memo[n] = 1 + (collatz(n // 2) if n % 2 == 0 else collatz(3 * n + 1))
  return memo[n]

res, mx = 0, 0
for i in range(1, 1000000):
  if collatz(i) > mx:
    res = i
    mx = memo[i]

print(res)