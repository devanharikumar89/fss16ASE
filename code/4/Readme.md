# Screenshots
* [Simulated Annealing](https://github.com/arjunaugustine/fss16ASE/blob/master/code/4/screenshots/h4_sa.png)

## Explanation
First step is to set baseline values. This includes the min_energy and max_energy for Schaffer function. This is currently done by generating 1000 random energy values and taking the maximum and minimum values out of the 1000 values. We also set enough energy which is 1 - epsilon values. In our Simulated annealing algorithm the temperature varies from 1 to 1000.

We start at a random state and energy and set it to the current state and energy. Then we generate a new state and energy. If this new state and energy is any improvement over the current state and energy, we set the new state to the current state. If this new state is better than the best state so far we make it the new best state.

If the new state and energy is not an improvement over the current state and energy, we rely on the probability function
to determine whether to move to this new state or not. The probability function takes into account the temperature to determine the probability. At low temperature there is a higher probability of the system moving to a new energy state even if this new state is worse. However, as the temerature increases this probability reduces. The system becomes sober. It would then follow a greedy approach and exit when we reach enough energy.

In the output, initially we can see lot of '?' which gradually decreases. We print a '?' every time we move to a state which is worse and this happens more when the temperature is low. Every time we encounter a new best we print a '!' and everytime we find a state better than current we print a '+'. So a '!' will always be followed by a '+'. We print a '.' for every iteration. The number of isolated '.' indicate that the iteration did not find any better state or energy.

At end we return the best state and its energy.
