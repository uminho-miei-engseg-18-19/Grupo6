# TP - 25/Fev/2019

## Question 1.1

After executing the command we saw, by testing, that our location was not USA. This arise from the fact that **TOR** client picks a random series of TOR nodes from a list, given by a Directory Server (a more trusted OR), to the destination server.  

## Question 1.2

When connecting to the website we can see 6 jumps, 3 of wich chosen by the OP that access the anonymous service, the third being the *Rendezvous* point, and the last 3 chosen by the anonymous service (Relays). This makes the both the OP that access and the OP being accessed anonymous. 