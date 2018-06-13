# Visualizing Random Processes

This is a quick tutorial for visualizing and developing a basic understanding of simple random walks, branching processes, and regime switching. As this is geared toward individuals who may not have taken a probability course yet, we're not going to get deep into the math here (Although if you are interested in the maths, [Gordan Zitkovic's Stochastic Processes notes](https://www.ma.utexas.edu/users/gordanz/notes/) can explain all of that better than I ever could). Rather, we're going to simulate these processes to see what is actually occuring over time.

Before we start, you might ask why we even care about random processes. Given that "because random processes are NEATO" isn't a satisfying answer for most people, let's consider some practical applications. We can use random walks to approximate price fluctuation in the stock market or to simulate the movement of molecules in liquids and gasses. Branching processes are useful for modeling reproduction, and the probability that a certain population will go extinct. I personally have made use of random processes as part of my ongoing attempts to [automatically map the Antarctic Ice Sheet.](https://github.com/AlyssaYelle/auto-piking)

In this tutorial we aren't going to apply these concepts to any problems -- that will come later. Rather, we're just going to visualize them in order to build up our intuition about what is happening behind all the maths.


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


## Branching Processes

Every once in a while a mathematical concept will arise from an individual with problematic views, and the branching process is one of them. Sir Francis Galton, also known as the father of eugenics, questioned how many male children each generation of a family would have to produce on average in order for the family line to not become extinct. After a collaboration with Henry William Watson, the branching process model was born.

Thankfully, branching processes have applications outside of eugenics. For example, we can use them to model whether a population of cancerous cells will become extinct before it grows large enough to overwhelm the surrounding tissue.

### Modeling a Single Branching Process

To model a branching process we want to start with a single individual, <a href="https://www.codecogs.com/eqnedit.php?latex=Z_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_0" title="Z_0" /></a>, at time n = 0, and assume that they will produce a random number of children before dying off. The number of children they can produce may only be a nonnegative integer, so we will model this random variable using a Poisson distribution with parameter lambda, where lambda is the expected value.

If our initial individual produces 0 children, the population is dead and nothing will happen at any time going forward. If they produce <a href="https://www.codecogs.com/eqnedit.php?latex=Z_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_1" title="Z_1" /></a> > 0 children, the children will then go on to reproduce as well. If none of them produce children, the population dies off. Otherwise, at time n = 2 we will have <a href="https://www.codecogs.com/eqnedit.php?latex=Z_2&space;=&space;\sum_{i&space;=&space;1}^{Z_1}Z_{1,i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_2&space;=&space;\sum_{i&space;=&space;1}^{Z_1}Z_{1,i}" title="Z_2 = \sum_{i = 1}^{Z_1}Z_{1,i}" /></a> individuals in the population. If it ever happens that Z_n = 0, our population is extinct. Otherwise, <a href="https://www.codecogs.com/eqnedit.php?latex=Z_{n&plus;1}&space;=&space;\sum_{i&space;=&space;1}^{Z_n}Z_{n,i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_{n&plus;1}&space;=&space;\sum_{i&space;=&space;1}^{Z_n}Z_{n,i}" title="Z_{n+1} = \sum_{i = 1}^{Z_n}Z_{n,i}" /></a>.

When I first learned about branching processes I found it difficult to really visualize what's going on simply based on the math, and coding it up really helped me out. So let's look at the code and generate some plots!

```r
#over multiple trials we will show that if population does not immediately die off it will explode

#initialize list of population size at generation n
Z<-1

#pop. size 1 at generation 0
Z[0] = 1

#poisson r.v.
#each member generates poisson(lambda) offspring
#sum offspring
lambda = 2
N = 20

Z[1] = rpois(Z[0], lambda)

for (i in 2:N)
{
  if(Z[i-1]==0) {Z[i]=0} else 
    {
      x=rpois(Z[i-1], lambda) 
      Z[i] = sum(x)
    }
}
Z
plot(Z, type = "l")
```

I like to run this simulation using lambda = 2 because over multiple trials we can clearly see that if the population does not die off within the first few generations, it will explode. See the plots below.

![alt text](https://github.com/AlyssaYelle/StochasticProcesses/blob/master/plots/branchpopdeath.png "Population death")
![alt text](https://github.com/AlyssaYelle/StochasticProcesses/blob/master/plots/branchpopexplode.png "Population explodes")


### Approximating the Probability of Extinction

Since branching processes are random, running a single simulation is rather worthless if we're seeking some kind of concrete information. For example, one question we could ask is *what is the probability that population reproducing itself from a Poisson(2) distribution will become extinct?*

If you've taken a class on stochastic processes then you know we can find this probability using generating functions, but what if you don't know what a generating function is? 

Well, if we can [simulate one branching process](https://github.com/AlyssaYelle/StochasticProcesses/blob/master/branching_process.R), we can [simulate hundreds of branching processes](https://github.com/AlyssaYelle/StochasticProcesses/blob/master/extinction_prob.py) and thus approximate the probability of extinction.

After simulating a Poisson(2) branching process 300 times, I found that the extinction probability is around 0.2, which is the same solution we would find using the generating function <a href="https://www.codecogs.com/eqnedit.php?latex=x&space;=&space;e^{(\lambda(x-1))}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x&space;=&space;e^{(\lambda(x-1))}" title="x = e^{(\lambda(x-1))}" /></a>.

## Regime Switching

What if we want to consider a system that has only two states? Some examples of such a system would be high/low volatility in a financial market, english/non-english text in a work of literature, or my personal favorite example, the presence of water or no water underneath an ice sheet.

We can represent these states as 0 and 1 and then construct a stochastic matrix where <a href="https://www.codecogs.com/eqnedit.php?latex=p_{00}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{00}" title="p_{00}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=p_{11}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{11}" title="p_{11}" /></a> are the probabilities of remaining in the current state and <a href="https://www.codecogs.com/eqnedit.php?latex=P_{10}&space;=&space;1&space;-&space;p_{11}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P_{10}&space;=&space;1&space;-&space;p_{11}" title="P_{10} = 1 - p_{11}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=P_{01}&space;=&space;1&space;-&space;p_{00}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P_{01}&space;=&space;1&space;-&space;p_{00}" title="P_{01} = 1 - p_{00}" /></a> are the probabilities of switching states:

<a href="https://www.codecogs.com/eqnedit.php?latex=P&space;=&space;\begin{bmatrix}&space;p_{00}&space;&&space;p_{01}&space;\\&space;p_{10}&space;&&space;p_{11}&space;\\&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P&space;=&space;\begin{bmatrix}&space;p_{00}&space;&&space;p_{01}&space;\\&space;p_{10}&space;&&space;p_{11}&space;\\&space;\end{bmatrix}" title="P = \begin{bmatrix} p_{00} & p_{01} \\ p_{10} & p_{11} \\ \end{bmatrix}" /></a>

The plot below was [generated](https://github.com/AlyssaYelle/StochasticProcesses/blob/master/markov_chain.py) using the stochastic matrix
 <a href="https://www.codecogs.com/eqnedit.php?latex=P&space;=&space;\begin{bmatrix}&space;0.95&space;&&space;0.05&space;\\&space;0.01&space;&&space;0.99&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P&space;=&space;\begin{bmatrix}&space;0.95&space;&&space;0.05&space;\\&space;0.01&space;&&space;0.99&space;\end{bmatrix}" title="P = \begin{bmatrix} 0.95 & 0.05 \\ 0.01 & 0.99 \end{bmatrix}" /></a>

![alt text](https://github.com/AlyssaYelle/StochasticProcesses/blob/master/plots/regime_switching.png "Regime Switching")


## Ref
- My own personal notes from [Stephen Walker's](https://stat.utexas.edu/component/cobalt/item/15-mathematics/385-walker-stephen-g?Itemid=1176) Stochastic Processes class at UT Austin
- [Gordan Zitkovic's](https://www.ma.utexas.edu/users/gordanz/) lecture notes on [random walks](https://www.ma.utexas.edu/users/gordanz/notes/lecture4.pdf) and [branching processes](https://www.ma.utexas.edu/users/gordanz/notes/lecture7.pdf)






