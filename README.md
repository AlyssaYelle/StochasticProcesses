# Visualizing Random Processes

This is a quick tutorial for visualizing and understanding simple random walks and branching processes.

## Simple Random Walks

A simple random walk with parameter *p* in (0,1) is a sequence {X_n} of random variables with the following properties:
1. X_0 = 0
2. X_n+1 - X_n is independent of (X_0, X_1, ..., X_n) for all n
3. The random variable X_n+1 - X_n has the following distribution:

-1    |1     
--- | ---
(1-*p*) |*p*    

Basically, at each time n+1, we take a step up with probability *p* or a step down with probability (1 - *p*).

We can visualize this process in R using just a few lines of code.

```r
# set probability of moving up at time t+1
# initialize set of moves and position at time = 0
p = 0.3
s = 0
s[1] = 0


# generate N = 100 random values in (0,1) 
# assign -1 if < p, 1 if >=p
N = 100

for(i in 2:N)
{
x = runif(1)
if(x<p) {s[i]=s[i-1]+1} else {s[i]=s[i-1]-1}
}  

# generate basic plot
plot(s, type ="l")
```



