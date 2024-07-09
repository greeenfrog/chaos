# Chaotic systems

Visualizations of chaotic systems using [Matplotlib](https://matplotlib.org/).

## Double pendulum

Modelled by the following second-order, non-linear differential equations:

$$m_2(g\sin(\theta_1)+l_2((\theta_2')^2\sin(\theta_1-\theta_2)+\theta_2''\cos(\theta_1-\theta_2))+l_1\theta_1'')+m_1(g\sin(\theta_1)+l_1\theta_1'')=0$$

$$g\sin(\theta_2)+l_1(\theta_1''\cos(\theta_1-\theta_2)-(\theta_1')^2\sin(\theta_1-\theta_2))+l_2\theta_2''=0$$

## Three body

Modelled by the following set of differential equations, with the vector position of each object as $r_i$.

$$\ddot r_1=-Gm_2\frac{r_1-r_2}{|r_1-r_2|^3}-Gm_3\frac{r_1-r_3}{|r_1-r_3|^3}$$

$$\ddot r_2=-Gm_3\frac{r_2-r_3}{|r_2-r_3|^3}-Gm_1\frac{r_2-r_1}{|r_2-r_1|^3}$$

$$\ddot r_3=-Gm_1\frac{r_3-r_1}{|r_3-r_1|^3}-Gm_2\frac{r_3-r_2}{|r_3-r_2|^3}$$
