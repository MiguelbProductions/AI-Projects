import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {
    "NumRooms": [2, 3, 4, 5, 4, 8, 2, 7, 1, 9],
    "SizeOfHouse": [50, 70, 80, 90, 85, 200, 40, 180, 30, 220],
    "Location": [3, 4, 2, 5, 4, 3, 2, 5, 1, 5],
    "PriceOfHouse": [100000, 117000, 168000, 158000, 145000, 295000, 95000, 274000, 58000, 285000]
}

df = pd.DataFrame(data)

X = df[["NumRooms", "SizeOfHouse", "Location"]]
y = df["PriceOfHouse"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.scatter(df["NumRooms"], df["PriceOfHouse"], color='blue')
plt.plot(df["NumRooms"], model.predict(df[["NumRooms", "SizeOfHouse", "Location"]]), color='red')
plt.xlabel('Number of Rooms')
plt.ylabel('House Price')

plt.subplot(1, 3, 2)
plt.scatter(df["SizeOfHouse"], df["PriceOfHouse"], color='blue')
plt.plot(df["SizeOfHouse"], model.predict(df[["NumRooms", "SizeOfHouse", "Location"]]), color='red')
plt.xlabel('Size of House (sqm)')

plt.subplot(1, 3, 3)
plt.scatter(df["Location"], df["PriceOfHouse"], color='blue')
plt.plot(df["Location"], model.predict(df[["NumRooms", "SizeOfHouse", "Location"]]), color='red')
plt.xlabel('Location Rating')

plt.tight_layout()
plt.show()
