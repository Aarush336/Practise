# Practise Question 5: Create a numpy array of the humidity readings from Question 3. Print the mean, max, and min. Then print only the readings above 70.
import numpy as np
humidity_reading = np.array([55, 70, 80, 45, 90, 60, 75])
print(humidity_reading.mean())
print(humidity_reading.max())
print(humidity_reading.min())
print(humidity_reading[humidity_reading > 70])