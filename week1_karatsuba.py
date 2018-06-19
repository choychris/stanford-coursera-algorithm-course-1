# my attempt :

def multipleac(a, c, compute):
  product = compute(a, c)
  return product

def multiplebd(b, d, compute):
  product = compute(b, d)
  return product

def getabcd(a, b, c, d):
  product = (int(a) + int(b)) * (int(c) + int(d))
  return product

def compute(input1, input2):
  n = len(input1)
  if(n >= 2):
    firstHalf = int(n/2)
    a = (input1)[:firstHalf]
    b = (input1)[firstHalf:]
    c = (input2)[:firstHalf]
    d = (input2)[firstHalf:]
    third = getabcd(a, b, c, d)
    # print('third', third)
    second = multiplebd(b, d, compute)
    # print('second', second)
    first = multipleac(a, c, compute)
    # print('first', (10**n * first))
    combine = third - second - first
    result = (10**n) * first + 10**int(n/2) * combine + second
    # print ('result', result)
    return int(result)
  else:
    resultSmall = int(input1) * int(input2)
    # print ('resultSmall', resultSmall)
    return resultSmall

# better alogrithm :

from math import ceil, floor
#math.ceil(x) Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
#math.floor(x) Return the floor of x as a float, the largest integer value less than or equal to x.

def karatsuba(x,y):
  #base case
  if x < 10 and y < 10: # in other words, if x and y are single digits
    return x*y

  n = max(len(str(x)), len(str(y)))
  m = int(ceil(float(n)/2))   #Cast n into a float because n might lie outside the representable range of integers.

  x_H  = int(floor(x / 10**m))
  x_L = int(x % (10**m))

  y_H = int(floor(y / 10**m))
  y_L = int(y % (10**m))

  #recursive steps
  a = karatsuba(x_H,y_H)
  d = karatsuba(x_L,y_L)
  e = karatsuba(x_H + x_L, y_H + y_L) -a -d

  return int(a*(10**(m*2)) + e*(10**m) + d)


