import math


while True:
    try:
        T = int(raw_input().strip())
        for i in range(T):
            [N, P, W, H] = [int(x) for x in raw_input().strip().split()]
            a = [int(arg) for arg in raw_input().strip().split()]
            S=min(W,H)
            rows=[math.ceil(a_i/int(W/S)) for a_i in a]
            Row=sum(rows)
            pages=math.ceil(Row/int(H/S))
            while pages > P:
                S=S-1
                rows=[math.ceil(a_i/int(W/S)) for a_i in a]
                Row=sum(rows)
                pages=math.ceil(Row/int(H/S))
            print S

    except EOFError:
        break
            # for S in xrange(min(W, H), 0, -1):
            #     cols = floor(W / S)
            #     row = floor(H / S)
            #     lines = [ceil(ai / cols) for ai in a]
            #     rows = sum(lines)
            #     pages = int(ceil(rows / row))
            #     if pages <= P and S > max_S:
            #         max_S = S
            # print max_S
