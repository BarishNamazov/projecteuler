for i in range(1, 1000):
  for j in range(i + 1, 1000):
    k = 1000 - i - j
    if i * i + j * j == k * k:
      print(i * j * k)
      exit(0) 