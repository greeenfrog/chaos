import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.80665
G = 6.6743e-11
t = 1

fig, ax = plt.subplots()
fig.set_size_inches(6, 6)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
path1 = ax.plot([], [], linewidth=0.5, c='r')[0]
path2 = ax.plot([], [], linewidth=0.5, c='g')[0]
path3 = ax.plot([], [], linewidth=0.5, c='b')[0]


class ThreeBody:
    def __init__(self, r1, r2, r3, m1=1e6, m2=1e6, m3=1e6, dr1=None, dr2=None, dr3=None):
        self.r1 = np.asarray(r1)
        self.r2 = np.asarray(r2)
        self.r3 = np.asarray(r3)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.dr1 = np.asarray(dr1 if dr1 is not None else [0, 0])
        self.dr2 = np.asarray(dr2 if dr2 is not None else [0, 0])
        self.dr3 = np.asarray(dr3 if dr3 is not None else [0, 0])
        self.path1x = []
        self.path1y = []
        self.path2x = []
        self.path2y = []
        self.path3x = []
        self.path3y = []

    def update(self, _):
        d2r1 = -G*self.m2*(self.r1-self.r2)/(np.sqrt(sum((self.r1-self.r2)**2))**3) - G*self.m3*(self.r1-self.r3)/(np.sqrt(sum((self.r1-self.r3)**2))**3)
        d2r2 = -G*self.m3*(self.r2-self.r3)/(np.sqrt(sum((self.r2-self.r3)**2))**3) - G*self.m1*(self.r2-self.r1)/(np.sqrt(sum((self.r2-self.r1)**2))**3)
        d2r3 = -G*self.m1*(self.r3-self.r1)/(np.sqrt(sum((self.r3-self.r1)**2))**3) - G*self.m2*(self.r3-self.r2)/(np.sqrt(sum((self.r3-self.r2)**2))**3)
        self.dr1 = self.dr1 + t*d2r1
        self.dr2 = self.dr2 + t*d2r2
        self.dr3 = self.dr3 + t*d2r3
        self.r1 = self.r1 + t*self.dr1
        self.r2 = self.r2 + t*self.dr2
        self.r3 = self.r3 + t*self.dr3
        self.path1x.append(self.r1[0])
        self.path1y.append(self.r1[1])
        self.path2x.append(self.r2[0])
        self.path2y.append(self.r2[1])
        self.path3x.append(self.r3[0])
        self.path3y.append(self.r3[1])
        if len(self.path1x) > 10000:
            self.path1x.pop(0)
            self.path1y.pop(0)
            self.path2x.pop(0)
            self.path2y.pop(0)
            self.path3x.pop(0)
            self.path3y.pop(0)
        print(self.r1, self.r2, self.r3)
        path1.set_xdata(self.path1x)
        path1.set_ydata(self.path1y)
        path2.set_xdata(self.path2x)
        path2.set_ydata(self.path2y)
        path3.set_xdata(self.path3x)
        path3.set_ydata(self.path3y)


tb = ThreeBody([0, 6], [-3, -2.5], [2, 1])
ani = FuncAnimation(fig=fig, func=tb.update, interval=0)
plt.show()
