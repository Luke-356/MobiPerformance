from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

class MachineLearningModel:
    """Class to handle machine learning tasks."""

    def __init__(self, file):
        self.file = file
        self.model = None

    def train_model(self):
        """Train a linear regression model."""
        try:
            df = pd.read_csv(self.file)
            X = df[["Performance_Score", "Camera_Score", "Battery_Score"]]
            y = df["Price"]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            self.model = LinearRegression()
            self.model.fit(X_train, y_train)
            print("Model trained.")
            print("Model R^2 score:", self.model.score(X_test, y_test))
        except FileNotFoundError:
            print(f"File {self.file} not found.")
