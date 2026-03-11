# Practise Question 3: Create a DataFrame with 4 plants — name, soil moisture, and days since last watered. Print the full table. Print only plants where days since last watered is above 3.
import pandas as pd

Data_frame = {
                "name" : ["Cactus", "Dandelion", "Daisy", "Sunflower"],
                "soil_moisture" : [False, True, True, False],
                "last_watered" : [10, 2, 7, 1],
}
df = pd.DataFrame(Data_frame)
print(df)
print(df[df["last_watered"] > 3])