#! encoding=utf-8

# Creation Date: 2017-03-31 20:19:57
# Created By: Heyi Tang

def expected_number(p, q):
    num = 1
    np = 1
    cur_p = p
    result = 0
    while cur_p < 1:
        result += cur_p * num * np
        num += 1
        np *= (1-cur_p)
        cur_p += q
    result += num * np
    return result


def solve(n, p, q):
    q = q / 100.0
    zero_result = expected_number(0, q)
    new_p = p
    result = 0
    for i in xrange(n):
        if new_p == 0:
            result += zero_result
            continue
        else:
            result += expected_number(new_p/100.0, q)
        new_p = new_p / 2
    return "%.2f" % result

if __name__ == "__main__":
    n, p, q = 2, 50, 75
    line = raw_input()
    p, q, n = map(int, line.split())
    print solve(n,p,q)
