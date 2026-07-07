# kesken
# käyrän piirto puuttuu

import matplotlib.pyplot as plot
import numpy as np


xArvot = np.array([71, 86, 64, 92, 83])
yArvot = np.random.randint(0,100, size=5)

sumArrays = np.concatenate((xArvot, yArvot))

filterCondition = sumArrays > 25

filteredArray = sumArrays[filterCondition]