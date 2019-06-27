# Desafio-Skyone
# test-skyone
Challenge !
!
Load Balancing is quite important in Cloud environments. We are always trying to minimize the
costs so we keep the number of servers as low as possible. On the other hand we know that
capacity and performance improves when we add more servers. The challenge is to keep the
servers as busy as possible under a certain load capacity.!
!
On our simulation environment, at each clock tick (time unit), users connect to available servers
and request the same task to be executed. Each task consumes Ttask ticks of time to get
accomplished and after that the user disconnects immediately.!
!
The servers are virtual machines that can be spin up immediately to accommodate new users.
Each servers costs $1.00 per clock tick and can handle with Umax number of simultaneous users.
You can terminate the empty servers. !
!
Your challenge is to build a program in Python that handles with the incoming users and assign
them to servers keeping the cost as low as possible.!
!
Input: A file where each line contains the number of new users for that tick.!
Output: A file where each line contains a list of the available servers at the end of that tick,
represented by the number of users on each server.!
