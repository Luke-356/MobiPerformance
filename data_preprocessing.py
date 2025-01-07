import pandas as pd
import numpy as np

class DataPreprocessor:
    """Class to handle data cleaning, preprocessing, and feature engineering."""

    def __init__(self, input_file):
        self.input_file = input_file
        self.df = None

    def load_data(self):
        """Load data from the CSV file."""
        try:
            self.df = pd.read_csv(self.input_file)
        except FileNotFoundError:
            raise ValueError(f"File {self.input_file} not found.")

    def clean_data(self):
        """Clean the dataset by removing missing values."""
        self.df = self.df.dropna()

    def add_price_column(self):
        """Add a simulated price column."""
        np.random.seed(42)
        self.df["Price"] = np.random.randint(300, 1200, size=len(self.df))

    def feature_engineering(self):
        """Create new features."""
        self.df["Performance_Score"] = self.df["SoC"].apply(lambda x: len(x.split()))
        self.df["Camera_Score"] = self.df["Camera"].apply(lambda x: len(x.split()))
        self.df["Battery_Score"] = self.df["Battery"].apply(lambda x: len(x.split()))
        self.df["Value_Score"] = (self.df["Performance_Score"] +
                                  self.df["Camera_Score"] +
                                  self.df["Battery_Score"]) / self.df["Price"]

    def save_data(self, output_file):
        """Save the cleaned and processed data."""
        self.df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")

    def preprocess(self):
        """Run all preprocessing steps."""
        self.load_data()
        self.clean_data()
        self.add_price_column()
        self.feature_engineering()
