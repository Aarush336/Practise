# Self-made dataset 

import pandas as pd
import numpy as np
Plants = {
    "name" : ["cactus", "Daisy", "Dandelion", "Rose", "Aloe-vera", "Hibiscus", "Tulsi", "Neem", "Sunflower", "Tomatoes"],
    "temperature" : [42, 36, 45, 40, 45, 36, 34, 41, 43, 39],
    "humidity" : [30, 50, 39, 60, 20, 45, 20, 45, 32, 50],
    "soil_moisture" : [30, 20, 35, 70, 50, 60, 30, 37, 40, 50],
    "days_since_last_watered" : [7, 6, 4, 1, 4, 2, 4, 3, 5, 2],
}
df = pd.DataFrame(Plants)
df["water_needed"] = np.where(((df["temperature"] > 39) & (df["humidity"] < 40) & (df["soil_moisture"] < 40) & (df["days_since_last_watered"] > 3)), "Yes", "No")
print(df)