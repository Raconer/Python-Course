def plus(a, b):
  # b is int or b is float
  if type(b) is int or type(b) is float:
    return a + b
  else:
    return None

print(plus(12, 5))