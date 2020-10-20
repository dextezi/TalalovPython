import platform
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.integrate as integrate

def V(x):
    if (abs(x) < 2):
        return (-2 - np.cos(np.pi * x / 2))
    elif (abs(x) >= 2 and x <= 4):
        return (0.5 * (-1 + np.cos(np.pi * x / 2)))

def approx(a, b):
    # return V(random.uniform(a, b))
    return V((b+a)/2)

x0 = -4
xn = 4
fig = plt.figure()
plt.xticks(np.arange(x0, xn, step=1))
plt.yticks(np.arange(x0, xn, step=1))
m = 10
epsilon = 0.76
while True:
    plt.cla()
    m += 1
    x = np.linspace(x0, xn, m+1)
    y = []
    e = 0
    for i, _ in enumerate(x[1:]):
        yv = approx(x[i], x[i+1])
        y.append(yv)
        e += integrate.quad(lambda a: abs(V(a) - yv), x[i], x[i+1])[0]      # by L1

    if e <= epsilon:
        for i, _ in enumerate(x[1:x.size-1]):
            plt.plot([x[i], x[i+1]], [y[i], y[i]],  c='red')
            plt.plot([x[i+1], x[i+1]], [y[i], y[i+1]],  c='red')
        plt.plot([x[x.size-2], x[x.size-1]], [y[x.size-2], y[x.size-2]], c='red')
        break


x = np.linspace(x0, xn, 100)
y = [V(v) for v in x]
plt.plot(x, y)
plt.show()
print("Задание No 1, Вариант No \n"
      ".\n"
      "ПМИп-1702а\n"
      "e2 = 0.57, x = [-4, 4]\n"
      "Python: ", platform.python_version(),
      "\nm = ", m, " e2 <= %.2f" % e)
