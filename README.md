# Understanding Random Processes

This is a quick tutorial for visualizing and understanding simple random walks and branching processes.

## Simple Random Walks

A simple random walk with parameter *p* in (0,1) is a sequence {X_n} of random variables with the following properties:
1. X_0 = 0
2. X_n+1 - X_n is independent of (X_0, X_1, ..., X_n) for all n
3. The random variable X_n+1 - X_n has the following distribution:
|-1    |1     |
|:----:|:----:|
|(1-p) |p     |


