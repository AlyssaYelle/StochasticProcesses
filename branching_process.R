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