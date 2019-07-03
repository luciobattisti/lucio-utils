# EM algorithm 

Let's consider a probabilistic model where we denote the observed variables by X and the latent variables by Z. θ represents the model parameters.

The goal is to maximize the likelihood function

![equation](https://latex.codecogs.com/gif.latex?p(X|\theta)&space;=&space;\sum_{Z}&space;p(X,Z|\theta))

If we introduce a distribution ![equation](https://latex.codecogs.com/gif.latex?q%28z%29) defined over the latent variables, for any choice of ![equation](https://latex.codecogs.com/gif.latex?q%28z%29) we have the following decomposition:

![equation](https://latex.codecogs.com/gif.latex?ln%28p%28X%7C%5Ctheta%29%29%20%3D%20%5Cmathcal%7BL%7D%28q%2C%5Ctheta%29&plus;KL%28q%7C%7Cp%29)

Where

![equation](https://latex.codecogs.com/gif.latex?%5Cmathcal%7BL%7D%28q%2C%5Ctheta%29%20%3D%20%5Csum_%7BZ%7Dq%28Z%29ln%5C%7B%5Cfrac%7Bp%28X%2CZ%7C%5Ctheta%29%7D%7Bq%28Z%29%7D%5C%7D)

![equation](https://latex.codecogs.com/gif.latex?KL%28q%7C%7Cp%29%20%3D%20-%5Csum_%7BZ%7Dq%28Z%29ln%5C%7B%5Cfrac%7Bp%28Z%7CX%2C%5Ctheta%29%7D%7Bq%28Z%29%7D%5C%7D)

Proof

![equation](https://latex.codecogs.com/gif.latex?p%28X%2CZ%7C%5Ctheta%29%20%3D%20p%28Z%7CX%2C%5Ctheta%29p%28X%7C%5Ctheta%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cmathcal%7BL%7D%28q%2C%5Ctheta%29%20%3D%20%5Csum_%7BZ%7Dq%28Z%29ln%5C%7B%5Cfrac%7Bp%28Z%7CX%2C%5Ctheta%29p%28X%7C%5Ctheta%29%7D%7Bq%28Z%29%7D%5C%7D%20%3D)

![equation](https://latex.codecogs.com/gif.latex?%3D%5Csum_%7BZ%7Dq%28Z%29%28ln%5C%7B%5Cfrac%7Bp%28Z%7CX%2C%5Ctheta%29%7D%7Bq%28Z%29%7D%5C%7D&plus;p%28X%7C%5Ctheta%29%29%20%3D)

![equation](https://latex.codecogs.com/gif.latex?%3D-KL%28q%2Cp%29&plus;p%28X%7C%5Ctheta%29%5Csum_%7BZ%7Dq%28Z%29%3D-KL%28q%2Cp%29&plus;p%28X%7C%5Ctheta%29)

Since ![equation](https://latex.codecogs.com/gif.latex?KL%28q%7C%7Cp%29%3E%3D0),  ![equation](https://latex.codecogs.com/gif.latex?%5Cmathcal%7BL%7D%28q%2C%5Ctheta%29)is a lower bound of ![equation](https://latex.codecogs.com/gif.latex?ln%28p%28X%7C%5Ctheta%29%29). This simplifies the maximization problem a lot. In fact, if we maximize $ \mathcal{L}(q,\theta) $ we necessarily maximize $ln(p(X|\theta))$. 

Here we maximize the lower bound first respect to the distribution $ q(z) $ then to the parameters $ \theta $. If we observe the form of the KL divergency we notice that the lower bound reaches its maximum when KL = 0. This happens when $ q(Z) = p(Z | X, \theta) $.

We subsequently maximize the lower bound respect to $\theta$. This will cause the lower bound to go up. Since the KL divergency is not null because q(z) cannot equal the new posterior  $ p(Z | X, \theta^{new}) $, the likelihood will increase more than the lower bound. 

Overall, the optimization process consists of cycling through two steps: the expectation step where we set $ q(Z) = p(Z | X, \theta^{i}) $; and the maximization step where we maximize the lower bound respect to $\theta$ and $q(Z)$ is fixed. We repeat the cycle until the likelihood increments are smaller than a predefined values. 

Possibly the most important advantage of Expectation Maximization over plain likelihood optimization is the fact that the if subsistute $ q(z) = p(Z | X,\theta^{old})$ in the expression for the lower bound, we find out that the following form:

$ \mathcal{L}(q,\theta) = \sum_{Z}p(Z|X,\theta^{old}) \ln p(X,Z|\theta))-\sum_{Z}p(Z|X,\theta^{old}) \ln p(Z|X,\theta^{old}))$

We can notice that the term depending on $ \theta $ is in logartimic form. If the join distribution is a member of the exponential family, the maximization process would be greatly simplified. 



## Expectation step

 Maximize lower bound respect to $q(z)$ and keep $\theta$ fixed. The values of $\theta$ comes from the previous step.

## Maximization step  

Maximize upper bound respect to $\theta$ and keep $q(z)$ fixed. The distribution $q(z)$ comes from the previous step.







 

