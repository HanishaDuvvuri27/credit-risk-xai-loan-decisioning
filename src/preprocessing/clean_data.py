import pandas as pd

def load_and_clean_data(path):
    df = pd.read_excel(path, header=1)

    # Rename target
    df.rename(columns={"default payment next month": "default"}, inplace=True)

    # Drop ID column
    df.drop(columns=["ID"], inplace=True)

    return df

if __name__ == "__main__":
    df = load_and_clean_data("data/raw/default of credit card clients.xls")
    df.to_csv("data/processed/credit_default_clean.csv", index=False)
