import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.80665
t = 1e-2

fig, ax = plt.subplots()
fig.set_size_inches(6, 6)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
path = ax.plot([], [], linewidth=0.5, c='k')[0]
line = ax.plot([], [], c='k')[0]


class Pendulum:
    def __init__(self, theta, r=1):
        self.theta = theta
        self.dtheta = 0
        self.r = r

    def update(self, _):
        print(self.theta)
        d2theta = 2*g*np.sin(self.theta) / self.r
        self.dtheta += d2theta * t
        self.theta -= self.dtheta * t
        x = self.r * np.sin(self.theta)
        y = -self.r * np.cos(self.theta)
        line.set_xdata((0, x))
        line.set_ydata((0, y))


class DoublePendulum:
    def __init__(self, theta1, theta2, r1=0.5, r2=0.5, m1=1, m2=1):
        self.theta1 = theta1
        self.theta2 = theta2
        self.r1 = r1
        self.r2 = r2
        self.m1 = m1
        self.m2 = m2
        self.dtheta1 = 0
        self.dtheta2 = 0
        self.d2theta1 = 2*g*np.sin(self.theta1) / self.r1
        self.d2theta2 = 2*g*np.sin(self.theta2) / self.r2
        self.pathx = []
        self.pathy = []

    def update(self, _):
        diff_theta = self.theta1 - self.theta2
        self.d2theta1 = -(self.m2*(g*np.sin(self.theta1) + self.r2*(self.dtheta2**2)*np.sin(diff_theta) + self.r1*(self.dtheta1**2)*np.sin(diff_theta)*np.cos(diff_theta) - g*np.sin(self.theta2)*np.cos(diff_theta)) + self.m1*g*np.sin(self.theta1)) / (self.m2*self.r1*np.sin(diff_theta)**2 + self.m1*self.r1)
        self.d2theta2 = (self.r1*((self.dtheta1**2)*np.sin(diff_theta) - self.d2theta1*np.cos(diff_theta)) - g*np.sin(self.theta2)) / self.r2
        self.dtheta1 += t * self.d2theta1
        self.dtheta2 += t * self.d2theta2
        self.theta1 += t * self.dtheta1
        self.theta2 += t * self.dtheta2
        x1 = self.r1 * np.sin(self.theta1)
        y1 = -self.r1 * np.cos(self.theta1)
        x2 = x1 + self.r2 * np.sin(self.theta2)
        y2 = y1 - self.r2 * np.cos(self.theta2)
        self.pathx.append(x2)
        self.pathy.append(y2)
        if len(self.pathx) > 10000:
            self.pathx.pop(0)
            self.pathy.pop(0)
        print(self.theta1, self.theta2)
        line.set_xdata((0, x1, x2))
        line.set_ydata((0, y1, y2))
        path.set_xdata(self.pathx)
        path.set_ydata(self.pathy)


# p = Pendulum(np.pi/4)
p = DoublePendulum(np.pi/2, np.pi/2, r1=0.5, r2=0.5)
ani = FuncAnimation(fig=fig, func=p.update, interval=0)
plt.show()
