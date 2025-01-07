import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class DataVisualizer:
    """Class to handle data visualization."""

    @staticmethod
    def plot_price_vs_value(file):
        """Generate a scatter plot of price vs value score."""
        try:
            df = pd.read_csv(file)
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df, x="Price", y="Value_Score", hue="Model", size="Value_Score", palette="viridis")
            plt.title("Price vs Value Score")
            plt.xlabel("Price (USD)")
            plt.ylabel("Value Score")
            plt.legend(loc="upper right")
            plt.show()
        except FileNotFoundError:
            print(f"File {file} not found.")
