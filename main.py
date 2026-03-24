from scraper.scraper import scrape_books
from scraper.parser import clean_data
from scraper.validator import validate_data
import pandas as pd

def run_pipeline():
    scrape_books()
    df = clean_data()
    validated = validate_data(df)

    clean_df = pd.DataFrame(validated)
    clean_df.to_csv("data/cleaned.csv", index=False)

    print("Pipeline completed. Data saved.")


if __name__ == "__main__":
    run_pipeline()
