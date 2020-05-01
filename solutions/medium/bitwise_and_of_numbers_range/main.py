#!/usr/bin/env python

# Although there is a loop in the algorithm, the number of iterations is bounded by the number of bits that an integer has, which is fixed.
def bit_shift(m: int, n: int) -> int:
    shifts = 0
    while m != n:
        m >>= 1
        n >>= 1
        shifts += 1
    return 1 << shifts

    # if n >= 2 * m:
    #     return 0
    # else:
    #     r = m
    #     # time complexity is O(n - m)
    #     for i in range(m + 1, n + 1):
    #         r &= i
    #     return r


if __name__ == '__main__':
    print(bit_shift(4, 6))
