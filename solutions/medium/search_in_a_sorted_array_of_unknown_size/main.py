#!/usr/bin/env python

class ArrayReader:
    def get(self, index: int) -> int: ... 


class Solution:
    def search(self, reader: 'ArrayReader', t: int) -> int:
        l, r = 0, 2 ** 31 - 1

        while l <= r:
            mid = l + (r - l) // 2
            val = reader.get(mid)

            if val == t:
                return mid
            elif reader.get(mid) < t:
                l = mid + 1
            else:
                r = mid - 1

        return -1


if __name__ == '__main__':
    Solution().search(ArrayReader(), 2)
    ...
