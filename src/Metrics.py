import numpy as np
import pandas as pd
from scipy import stats
from math import sqrt



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


def sample_disease(df, n,seed=42):
    np.random.seed(seed)
    pop = df["disease"].to_numpy()
    sample = np.random.choice(pop,size=n,replace=True)
    
    return sample.mean()



def compare_disease(p_real, p_sim):
    diff = p_sim - p_real
    rel_diff = (diff / p_real) * 100
    
    return diff, rel_diff


def bootstrap(df,B=3000):
   x = df["systolic_bp"].dropna()

   boot_means = np.empty(B)
   for b in range(B):
       sample = x.sample(n=len(x),replace=True)
       boot_means[b] = sample.mean()
       
   lower = np.percentile(boot_means,2.5)
   upper = np.percentile(boot_means, 97.5)

   return lower,upper,boot_means

def ci_mean_normal(x, confidence=0.95):
    x = np.asarray(x, dtype = float)

    mean_x =float(np.mean(x))
    s = float(np.std(x, ddof = 1))
    n = len(x)

    z_critical = 1.96

    half_width = z_critical * s / sqrt(n)
    lo = mean_x - half_width
    hi = mean_x + half_width

    return lo, hi, mean_x, s, n

def smoker_t_test(df):

    smokers = df[df["smoker"] == "Yes"]["systolic_bp"].to_numpy()
    non_smoker = df[df["smoker"] == "No"]["systolic_bp"].to_numpy()

    t_stat, p_val = stats.ttest_ind(smokers, non_smoker, equal_var = True)
    t_stat_w, p_val_w = stats.ttest_ind(smokers, non_smoker, equal_var = False)

    return t_stat,p_val,t_stat_w, p_val_w


