import numpy
import matplotlib.pyplot as plt
import random

anos = range(1980, 2011, 1)

data = []
data2 = []
for i in range(0, 31):
    a = random.randrange(10,56)
    b = random.randrange(5,67)
    data.append(a)
    data2.append(b)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(anos, data, label='teste1')
ax2.plot(anos, data2, label='teste2')
ax1.set_xlabel('anos')
ax1.set_ylabel('dado falso')
ax1.legend()
plt.show()
