import pandas as pd  # Import pandas for data manipulation
import matplotlib.pyplot as plt  # Import matplotlib for data visualization
from sklearn.model_selection import train_test_split  # Import train_test_split for splitting data
from sklearn.linear_model import LinearRegression  # Import LinearRegression for creating the model
from sklearn.metrics import mean_squared_error  # Import mean_squared_error for model evaluation

# Step 2: Loading Data
# Create a dictionary with study hours and exam scores
data = {
    'StudyHours': [1, 2, 3, 4, 5],
    'ExamScore': [1.5, 2.0, 2.5, 3.5, 3.0]
}
# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Preparing the Data
# Extract the feature (input) column 'StudyHours'
X = df[['StudyHours']]
# Extract the target (output) column 'ExamScore'
y = df['ExamScore']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Training the Model
# Create an instance of the LinearRegression model
model = LinearRegression()
# Train the model using the training data
model.fit(X_train, y_train)

# Step 5: Making Predictions
# Predict the exam scores for the test set
y_pred = model.predict(X_test)

# Step 6: Evaluating the Model
# Calculate the mean squared error between actual and predicted values
mse = mean_squared_error(y_test, y_pred)
# Print the mean squared error
print(f"Mean Squared Error: {mse}")

# Step 7: Visualizing the Results
# Create a scatter plot of the original data points
plt.scatter(X, y, color='blue')
# Plot the regression line (predicted values)
plt.plot(X, model.predict(X), color='red')
# Label the x-axis
plt.xlabel('Study Hours')
# Label the y-axis
plt.ylabel('Exam Score')
# Display the plot
plt.show()
