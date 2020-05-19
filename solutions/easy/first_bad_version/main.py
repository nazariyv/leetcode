#!/usr/bin/env python
import time


# Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version. 

# [false, false, false, true, true]
# [1,       2,     3,     4,    5]
# mid is 3, it is not bad, then look at range [3, 4, n]

# [false, false, true, false, false]
# [1,       2,     3,    4,     5]
# mid is 3, it is bad, then look at range [1, 2, 3]

# look until two adjacent items and they are [false, true]


def isBadVersion(n: int) -> bool:
    if n < 2:
        return False
    return True


def firstBadVersion(n: int) -> int:

    def determine_bad_version(lo: int, hi: int) -> int:
        if lo == hi: return lo
        while lo + 1 != hi:
            print(f"{lo}-{hi}")
            time.sleep(2)
            mid = (lo + hi) // 2
            is_bad = isBadVersion(mid)
            if is_bad: hi = mid
            else:      lo = mid
        if isBadVersion(lo):
            return lo
        return hi

    return determine_bad_version(1, n)


if __name__ == '__main__':
    firstBadVersion(10)
    ...
