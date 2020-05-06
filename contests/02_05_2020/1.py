#!/usr/bin/env python


def candies(cands: List[int], extraCandies: int) -> List[bool]:
    largest = max(cands)
    return [cand + extraCandies >= largest for cand in cands]
