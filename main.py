from data_collection import DataCollector
from data_preprocessing import DataPreprocessor
from data_visualization import DataVisualizer
from machine_learning import MachineLearningModel
import pandas as pd

def main():
    collector = DataCollector("https://en.wikipedia.org/wiki/Comparison_of_smartphones")
    collector.fetch_data()

    preprocessor = DataPreprocessor("wikipedia_smartphones.csv")
    preprocessor.preprocess()
    preprocessor.save_data("value_smartphones.csv")

    DataVisualizer.plot_price_vs_value("value_smartphones.csv")

    ml_model = MachineLearningModel("value_smartphones.csv")
    ml_model.train_model()

    # Identify the phone with the highest value score
    df = pd.read_csv("value_smartphones.csv")
    best_phone = df.loc[df["Value_Score"].idxmax()]
    print("Phone with the highest value score:")
    print(best_phone)

if __name__ == "__main__":
    main()
