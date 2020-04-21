start top left

spawn two "runners", one going right and the other going down
keep the global values for the path cost of all runners. Also keep
the cost of minimum runner. Only proceed the minimum runner at any point in time.

Whoever gets to the finish first, is the minimum runner. Is this claim correct?

runners should be stored as follows:
{
    (row_ix, col_ix): cumulative_cost
}

should also keep an index of the minimum runner at any one point at time
