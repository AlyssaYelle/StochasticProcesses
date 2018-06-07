# Visualizing Random Processes

This is a quick tutorial for visualizing and developing a basic understanding of simple random walks and branching processes. We're not going to get deep into the math here ([Gordan Zitkovic's Stochastic Processes notes](https://www.ma.utexas.edu/users/gordanz/notes/) can explain all of that better than I ever could), rather we're going to simulate these processes to see what is actually occuring over time.

Before we start, you might ask why we even care about random processes. Given that "because random processes are NEATO" isn't a satisfying answer for most people, let's consider some practical applications. We can use random walks to approximate price fluctuation in the stock market or to simulate the movement of molecules in liquids and gasses. Branching processes are useful for modeling reproduction, and the probability that a certain population will go extinct. 

## Simple Random Walks

A simple random walk with parameter <a href="https://www.codecogs.com/eqnedit.php?latex=p&space;\in&space;(0,&space;1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p&space;\in&space;(0,&space;1)" title="p \in (0, 1)" /></a> is a sequence <a href="https://www.codecogs.com/eqnedit.php?latex=\{X_n\}_{n&space;\in&space;\mathbb{N}_0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\{X_n\}_{n&space;\in&space;\mathbb{N}_0}" title="\{X_n\}_{n \in \mathbb{N}_0}" /></a> of random variables with the following properties:
1. <a href="https://www.codecogs.com/eqnedit.php?latex=X_0&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_0&space;=&space;0" title="X_0 = 0" /></a>
2. <a href="https://www.codecogs.com/eqnedit.php?latex=X_{n&plus;1}&space;-&space;X_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_{n&plus;1}&space;-&space;X_n" title="X_{n+1} - X_n" /></a> is independent of <a href="https://www.codecogs.com/eqnedit.php?latex=\(X_0,&space;X_1,&space;...,&space;X_n\)&space;\forall&space;n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\(X_0,&space;X_1,&space;...,&space;X_n\)&space;\forall&space;n" title="\(X_0, X_1, ..., X_n\) \forall n" /></a>
3. The random variable <a href="https://www.codecogs.com/eqnedit.php?latex=X_{n&plus;1}&space;-&space;X_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_{n&plus;1}&space;-&space;X_n" title="X_{n+1} - X_n" /></a> has the following distribution:

-1    |1     
--- | ---
(1-*p*) |*p*    

Basically, at each time n+1, we take a step up with probability *p* or a step down with probability (1 - *p*).

We can visualize this process in R using just a few lines of code.

```r
# set probability of moving up at time t+1
# initialize set of moves and position at time = 0
p = 0.5
s = 0
s[1] = 0


# generate N = 100 random values from a Uniform(0,1) distribution 
# assign 1 if < p, -1 if >=p
N = 100

for(i in 2:N)
{
x = runif(1)
if(x<p) {s[i]=s[i-1]+1} else {s[i]=s[i-1]-1}
}  

# generate basic plot
plot(s, type ="l")
```

What does this actually look like, though? Let's look at plots for *p* = 0.4, 0.5, and 0.9.

![alt text](https://github.com/AlyssaYelle/StochasticProcesses/blob/master/plots/randwalkp4.png "p = 0.4")

![alt text](https://github.com/AlyssaYelle/StochasticProcesses/blob/master/plots/symrandwalk.png "p = 0.5")

![alt text](https://github.com/AlyssaYelle/StochasticProcesses/blob/master/plots/randwalkp9.png "p = 0.9")

Now, it's important to remember that while these processes are beholden to some probability distribution, they are *random*. For any random walk with parameter *p* I could run the simulation 10 times and produce 10 different plots.




