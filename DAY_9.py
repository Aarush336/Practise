import pandas as pd
import numpy as np

np.random.seed(42)
n = 100

temperature = np.random.randint(25, 50, n)
humidity = np.random.randint(15, 80, n)
soil_moisture = np.random.randint(10, 80, n)
days_since_watered = np.random.randint(1, 14, n)

df = pd.DataFrame({
    "temperature" : temperature,
    "humidity" : humidity,
    "soil_moisture" : soil_moisture,
    "days_since_watered" : days_since_watered,
})

df["water_needed"] = np.where(
    ((df["temperature"] > 39)
    &
    (df["soil_moisture"] < 40))
    |
    ((df["temperature"] > 39)
    &
    (df["days_since_watered"] > 3))
    |
    ((df["humidity"] < 40 )
    &
    (df["soil_moisture"] < 40)),
    "Yes", "No"
)
print(df["water_needed"].value_counts())

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X = df[["temperature", "humidity", "soil_moisture", "days_since_watered"]]
Y = df["water_needed"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=42)

from sklearn.metrics import accuracy_score

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
prediction = model.predict(X_test)
accuracy = accuracy_score(Y_test, prediction)
print(accuracy)
