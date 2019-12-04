"""Returns maximum values given ranges and weight per range.

In order to find the maximum value, construct an array of
slop, by adding at x - 1 and removing at y, so that when doing
the cummulation, we end up with a result array containing the
range.

x y w
1 5 10
4 9 5

10  0  0  0  0 -10  0  0  0  0
 0  0  0  5  0  0   0  0  0  -5
---
10 10 10 15 15  5   5  5  5  0


Resulting in O(n+1)
"""


def arrayManipulation(n, queries):
    res = [0] * (n + 1)

    for q in queries:
        x, y, incr = q[0], q[1], q[2]

        res[x - 1] += incr

        if y <= len(res):
            res[y] -= incr

    mx = 0
    x = 0
    for i in res:
        x = x + i
        if mx < x:
            mx = x

    return mx
