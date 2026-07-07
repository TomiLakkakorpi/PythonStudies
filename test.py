import matplotlib.pyplot as plt
import numpy as np

xData = [1,2,3,4,5]
yData = [8, 1, 5, 9, 6]
varitys = ["gray","gray","gray","gray","gray"]

xArvo = np.array(xData)
yArvo = np.array(yData)
colorList = np.array(varitys)

plt.subplot(2,3,1)
plt.bar(xArvo,yArvo,color=colorList)
plt.show()

