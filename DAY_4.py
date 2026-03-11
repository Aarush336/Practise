# Practise Question 4: Using the same DataFrame from Question 3, print the average days since last watered. Then print the shape of the table.
import pandas as pd

Data_frame = {
                "name" : ["Cactus", "Dandelion", "Daisy", "Sunflower"],
                "soil_moisture" : [False, True, True, False],
                "last_watered" : [10, 2, 7, 1],
}
df = pd.DataFrame(Data_frame)
print(df["last_watered"].mean())
print(df.shape)