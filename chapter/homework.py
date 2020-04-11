# plus, minus, times, division, negation, power, reminer

def plus(x, y):
  x = convert_str_int(x)
  y = convert_str_int(y)
  return x + y

def minus(x, y):
  x = convert_str_int(x)
  y = convert_str_int(y)
  return x - y

def times(x, y):
  x = convert_str_int(x)
  y = convert_str_int(y)
  return x * y

def devision(x, y):
  x = convert_str_int(x)
  y = convert_str_int(y)
  return x / y

def negation(x):
  x = convert_str_int(x)
  return -x

def power(x, y):
  x = convert_str_int(x)
  y = convert_str_int(y)
  return pow(x, y)

def reminder(x, y):
  x = convert_str_int(x)
  y = convert_str_int(y)
  return x % y

def convert_str_int(x):
  if isinstance(x, str):
    x = int(x)
  
  return x

x = 5
y = 3
z = "5"
r = "3"

print("plus"      , plus(x, y))
print("minus"     , minus(x, y))
print("times"     , times(x, y))
print("devision"  , devision(x, y))
print("negation"  , negation(x))
print("power"     , power(x, y))
print("reminder"  , reminder(x, y))
print()
print("plus"      , plus(z, r))
print("minus"     , minus(z, r))
print("times"     , times(z, r))
print("devision"  , devision(z, r))
print("negation"  , negation(z))
print("power"     , power(z, r))
print("reminder"  , reminder(z, r))