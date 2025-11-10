import pandas as pd
import numpy as np

def load_csv(filepath):
    return pd.read_csv(filepath)

def clean_df(df):
    df.columns = [c.strip() for c in df.columns]
    df["sex"] = df["sex"].astype(str).str.strip().upper()
    df["smoker"] = df["smoker"].astype(str).str.strip().capitalize()
    df["cholesterol"] = pd.to_numeric(df["cholesterol"],errors = "coerce")
    df["disease"] = pd.to_numeric(df["disease"],errors= "coerce")
    df = df.dropna(subset=["weight","height","systolic_bp","cholesterol"])
    df["disease"] = df["disease"].astype(int)
    return df

def load_and_clean(filepath):
    df = load_csv(filepath)
    df = clean_df(df)
    return df

print(clean_df)