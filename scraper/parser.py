import pandas as pd
import json

def clean_data():
    with open("data/raw.json") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Clean price (£51.77 → 51.77)
    df["price"] = df["price"].str.replace("£", "").astype(float)

    # Normalize availability
    df["availability"] = df["availability"].str.replace("\n", "").str.strip()

    return df
