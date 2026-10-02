# GECISort
## Generate Every Combination Inefficiently Sort

- Time complexity: O(N^N * N)
- Extra space: O(N^(N+1))

## How It works
- Generate every possible combination of N elements (meaning a specific element can be used an indefinite number of times)
- For each of them, check whether they are sorted, and if they are, check whether each element occurs the same number of times as the original, unsorted array.

# WARNING
- This algorithm takes an insane amount of processing power as well as memory. For an input with a length of 10, it will require several hundred GIGABYTES of memory. Run it at your own risk.