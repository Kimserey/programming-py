def get_min(q):
    res = 0
    q = [p - 1 for p in q]

    for i, v in enumerate(q):
        diff = v - i

        if diff > 2:
            print("Too chaotic")
            return

        # Look in front by two positions,
        # as that's the maximum a value can
        # be swap to.
        for j in range(max(v - 1, 0), i):
            if q[j] > v:
                res += 1

    print(res)


# get_min([2, 1, 5, 3, 4])
get_min([1, 2, 5, 3, 7, 8, 6, 4])
