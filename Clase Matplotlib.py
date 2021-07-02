"""
CLASE MATPLOTLIB

"""

import matplotlib.pyplot as plt 

# Data for graph

x1 = [2000, 2005, 2010, 2015]
y1 = [110, 220, 330, 440]

x2 = [2000, 2005, 2010, 2015]
y2 = [400, 1200, 1800, 4500]

x3 = [2000, 2005, 2010, 2015]
y4 = y2 = [400, 1200, 1800, 4500]

plt.plot(x1, y1, color = 'red', linewidth = 2, label = 'Col')
plt.plot(x2, y2, color = 'green', linewidth = 2, label = 'Usa')
plt.bar(x3, y4, width= 0.8)
plt.title('Primer Gráfico',)
plt.xlabel('años')
plt.ylabel('Pibpc')
plt.legend()
#plt.grid()
plt.show()
