import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-20,20)
y=[]
for item in x:
    if item > 0:
        y.append(2 * np.sqrt(item) + item ** 2 + 2 * item)
    else:
        y.append(item ** 2 + 2 * item)

plt.plot(x,y,label="f(x)=2*x^(1/2) + x^2 + 2*x")
plt.title("wykres funkcji")
plt.xlabel("oś x")
plt.ylabel("oś y")
legend=plt.legend(loc="lower right")


plt.show()

