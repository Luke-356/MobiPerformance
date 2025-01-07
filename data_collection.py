import requests
from bs4 import BeautifulSoup
import pandas as pd

class DataCollector:
    """Class to handle data collection from a web source."""

    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def fetch_data(self):
        """Fetch data from the URL and save it as a CSV file."""
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find("table", {"class": "wikitable"})
            if not table:
                raise ValueError("No table found on the page.")

            headers = [header.text.strip() for header in table.find_all("th")]
            rows = [
                [cell.text.strip() for cell in row.find_all("td")]
                for row in table.find_all("tr")[1:]
                if row.find_all("td")
            ]

            df = pd.DataFrame(rows, columns=headers)
            df.to_csv("wikipedia_smartphones.csv", index=False)
            print("Data saved to wikipedia_smartphones.csv")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
