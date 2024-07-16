import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {
    "NumRooms": [2, 3, 4, 5, 4, 8, 2, 7, 1, 9],
    "PriceOfHouse": [100000, 117000, 168000, 158000, 145000, 295000, 95000, 274000, 58000, 285000]
}

df = pd.DataFrame(data)

X = df[["NumRooms"]]
y = df["PriceOfHouse"]

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, y, test_size=0.3)

model = LinearRegression()

model.fit(X_Train, Y_Train)

Y_Predict = model.predict(X_Test)

mse = mean_squared_error(Y_Test, Y_Predict)

print("Mean Squared error: ", mse)

plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Number of Rooms')
plt.ylabel('House Price')
plt.show()