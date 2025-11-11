import numpy as np
import pandas as pd
import math

def colums_description(df, cols):
    result = {}
    for col in cols:
        x = df[col].dropna().to_numpy()
        result[col] = {
            "mean": np.mean(x),
            "median": np.median(x),
            "min": np.min(x),
            "max": np.max(x)
        }
    return pd.DataFrame(result).T


def proportion_of_disease(df):
    return (df["disease"].mean())
