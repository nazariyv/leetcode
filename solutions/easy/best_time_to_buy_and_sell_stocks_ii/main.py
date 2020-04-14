#!/usr/bin/env python
from typing import List

# [7,1,5,3,6,4]   # possible trades: 1-5, 3-6. From these, pick the ones that maximize the profit
# [1,2,3,4,5]     # possible trades: 1-5
# [1,2,5,4,5]     # possible trades: 1-2, if increase after 2, then never want to trade 2-5 (because can trade 1-5)
# [7,6,4,3,1]     # no trades
# 1. ix = 0, if next is smaller, no trade
# 2. ix = 1, if next is higher = potential trade
# 3. ix = 2, if next is smaller -> potential trade complete, add to set
# 4. ix = 3, if next is higher = potential trade
# 5. ix = 4, if next is smaller -> potential trade complete, add to set

# once all the potential trades are ready, need to find the combination that yields
# highest total return, under
def calc_profit(trades):
    max_profit = 0
    for buy, sell in trades: max_profit += sell[1] - buy[1]
    return max_profit

def main(l: List[int]):
    ln = len(l)
    if ln < 2: return 0
    buy, sell, trades = (0, l[0],), (1, l[1]), []

    for _ix, v in enumerate(l[1:]):
        ix = _ix + 1
        if v < sell[1] and buy[1] < sell[1] and buy[0] < sell[0]:
            trades.append((buy, sell))
            buy = ix, v,
            sell = -1, 0,
            continue
        elif v < buy[1]: buy = ix, v,; continue
        elif ix == ln - 1 and buy[1] < v: return v - buy[1] + calc_profit(trades)
        sell = ix, v,
    return calc_profit(trades)


if __name__ == "__main__":
    max_profit = main([6,1,3,2,4,7])
    print(max_profit)
