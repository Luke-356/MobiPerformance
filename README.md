# MobiPerformance

MobiPerformance is a data analysis project aimed at helping consumers find the best smartphones for their budget. By ranking smartphones based on their "Value Score," the project provides insights into smartphone performance, camera quality, battery life, and price.

## Features
- **Data Cleaning**: Ensures the dataset is accurate and free from inconsistencies.
- **Feature Extraction**: Extracts meaningful attributes like performance, camera quality, battery life, and price from the dataset.
- **Predictive Modeling**: Builds a model to predict smartphone prices based on key features.
- **Value Score Calculation**: Ranks smartphones based on a calculated "Value Score," combining multiple attributes to assess their overall value for money.

## Dataset Source
The dataset is sourced from a Wikipedia page on smartphone comparisons. It includes:
- Smartphone model names
- System-on-chip (SoC) specifications
- Camera specifications
- Battery life
- Prices

## Intended Outcome
1. **Smartphone Ranking**: Helps consumers identify the best smartphones for their budget using the "Value Score."
2. **Price Prediction**: Predicts smartphone prices based on performance, camera, and battery features.

## Setup and Usage

### Prerequisites
- Python 3.8 or above
- Required Python libraries (listed in `requirements.txt`)

### Steps to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/Luke-356/MobiPerformance.git
    ```
2. Navigate to the project folder:
    ```bash
    cd MobiPerformance
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Open the project folder in your preferred IDE.
5. Run the main script:
    ```bash
    python main.py
    ```

## Folder Structure
```plaintext
MobiPerformance/
├── data_collection.py          # Scripts for collecting data
├── data_preprocessing.py       # Scripts for cleaning and preparing data
├── data_visualization.py       # Scripts for visualizing data
├── machine_learning.py         # Scripts for training predictive models
├── main.py                     # Main entry point
├── requirements.txt            # List of dependencies
├── README.md                   # Project documentation
