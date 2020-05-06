# Solutions

To find a target in a rotated search array, we can first find the inflection point
and then do standard binary search tree. These would require two passes O(log N)

Finding inflection point:

"""Inflection point is defined as a sudden drop. For that we need at least
two numbers, they have to be adjacent.
So the termination condition is that lo + 1 == hi
then return hi

edge cases
-----------
if len of nums is 0, return -1
if len of nums is 1, return 0
if len of nums is 2, return 1 if the second element is smaller than the first, else 0

time complexity is O(log N)
space complexit is O(1)
"""
