# trange
Trange use for range the number
```
In [1]: from trange import Range

In [2]: list(Range(4, 6, 7))
Out[2]: [4]

In [3]: Range(4, 6, 7)
Out[3]: <generator object Range at 0x7fbc23654930>

In [4]: Range(6)
Out[4]: <generator object Range at 0x7fbc23654390>

In [5]: list(Range(6))
Out[5]: [0, 1, 2, 3, 4, 5]

In [6]: list(Range(0,6,0))
Out[6]: [0, 1, 2, 3, 4, 5]

In [7]: list(range(0,6,0))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-7-3423f0478b5c> in <module>()
----> 1 list(range(0,6,0))

ValueError: range() arg 3 must not be zero

In [8]: list(Range(1,6,2))
Out[8]: [1, 3, 5]

In [9]: list(range(1,6,2))
Out[9]: [1, 3, 5]
```

