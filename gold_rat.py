def gold_rat(x1, x2, x3, x4, a, b, E):
    #step 2
    k = 0

    #step 3
    yk = a + (3 - 5 ** 0.5)/2 * (b - a)
    zk = a + b - yk

    while 1:
        #step 4
        fy = x1 * yk ** 3 + x2 * yk ** 2 + x3 * yk + x4
        fz = x1 * zk ** 3 + x2 * zk ** 2 + x3 * zk + x4

        #step 5
        if fy <= fz:
            a = a
            b = zk
            zk = yk
            yk = a + b - yk
        else:
            a = yk
            b = b
            yk = zk
            zk = a + b - zk

        #step 6
        delta = abs(a - b)
        if delta < E:
            seek_x = (a + b) / 2
            return seek_x, k
        else:
            k += 1

