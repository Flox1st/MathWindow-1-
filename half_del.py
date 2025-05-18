def half_delil(x1, x2, x3, x4, a, b, E):
    #step 2
    k = 0

    #step 3
    xk = (a + b)/2
    fx = x1 * xk ** 3 + x2 * xk ** 2 + x3 * xk + x4
    L = b - a

    #step 4
    while 1:
        yk = a + L/4
        zk = b - L/4
        fy = x1 * yk ** 3 + x2 * yk ** 2 + x3 * yk + x4
        fz = x1 * zk ** 3 + x2 * zk ** 2 + x3 * zk + x4

        #step 5
        if fy < fx:
            b = xk
            a = a
            xk = yk
        else:
            #step 6
            if fz < fx:
                a = xk
                b = b
                xk = zk
            else:
                a = yk
                b = zk
                xk = xk

        #step 7
        L = abs(b - a)
        if L <= E:
            seek_x = xk
            return seek_x, k
        else:
            k += 1


