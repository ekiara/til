>>> for x in xrange(999,3005):
...     sum = x*1.16
...     c = math.ceil(sum)
...     f = math.floor(sum)
...     if sum == c or sum == f:
...         print(x, sum)

>>> for x in xrange(3005,6000):
...     sum = x*1.16
...     c = math.ceil(sum)
...     f = math.floor(sum)
...     if sum == c or sum == f:
...         print(x, sum)

2500, 2900
(3750, 4350.0)
(2750, 3190.0)
(2250, 2610.0)
(2000, 2320.0)
(1250, 1450.0)
