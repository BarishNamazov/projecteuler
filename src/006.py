def _sum(x):
  return (x * (x + 1) // 2)**2
def _sumsq(x):
  return x * (x + 1) * (2 * x + 1) // 6
print(_sum(100) - _sumsq(100))