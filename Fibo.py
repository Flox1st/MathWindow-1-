def Fibon(x1, x2, x3, x4, a, b, E, l):
    #step 2
    L = b - a
    N = round(L/l)

    F = [1, 1]
    for i in range(N - 1):
        x = F[-1]+ F[-2]
        F.append(x)

    #step 3
    k = 0

    #step 4
    yk = a + (F[N-2]/F[N]) * (b - a)
    zk = a + (F[N-1]/F[N]) * (b - a)

    #step 5
    while 1:
        fy = x1 * yk ** 3 + x2 * yk ** 2 + x3 * yk + x4
        fz = x1 * zk ** 3 + x2 * zk ** 2 + x3 * zk + x4

        #step 6
        if fy <= fz:
            a = a
            b = zk
            zk = yk
            yk = a + (F[N - k -3]/F[N - k -1]) * (b - a)
        else:
            a = yk
            b = b
            yk = zk
            zk = a + (F[N - k - 2]/F[N - k - 1]) * (b - a)

        #step 7
        if k == N - 3:
            yk = (a + b) / 2
            zk = yk
            fy = x1 * yk ** 3 + x2 * yk ** 2 + x3 * yk + x4
            fz = x1 * zk ** 3 + x2 * zk ** 2 + x3 * zk + x4
            if fy <= fz:
                a = a
                b = zk
            else:
                a = yk
                b = b

            seek_x = (a + b) / 2

            return seek_x, k
        else:
            k += 1


