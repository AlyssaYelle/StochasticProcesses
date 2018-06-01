#simulate simple random walk
#
#set probability of moving up at time t+1
#initialize set of moves
p<-0.5
s<-0


N = 1000
#initialize position at time 0
s[1] = 0
#generate N random values from Uniform(0,1) distribution
#assign 1 if < p, -1 if >=p
for(i in 2:N)
{
x = runif(1)
if(x<p) {s[i]=s[i-1]+1} else {s[i]=s[i-1]-1}
}  
plot(s, type ="l")

