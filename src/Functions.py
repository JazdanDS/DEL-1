from src.Utilities import load_and_clean
from src.Metrics import (
    colums_description,
    proportion_of_disease,
    sample_disease,
    compare_disease,
    bootstrap,
    ci_mean_normal,
    smoker_t_test,
)
from src.Analyzer import HealthAnalyzer
import numpy as np

def results_full():
    df = load_and_clean("Data/health_study_dataset.csv")
    cols = ["age", "weight", "height", "systolic_bp", "cholesterol"]
    stats_df = colums_description(df, cols)
    stats_df_rounded = stats_df.round(2)
    induviduals= len(df)
    sick_individuals= df["disease"].sum()
    p_real = proportion_of_disease(df)
    p_sim = sample_disease(df, n=1000, seed=42)
    diff, rel_diff = compare_disease(p_real, p_sim)
    lower,upper,boot_means = bootstrap(df,B=3000)
    x = df["systolic_bp"].dropna().to_numpy()
    lo, hi, mean_x, s, n = ci_mean_normal(x)
    t_stat, p_val, t_stat_w, p_val_w = smoker_t_test(df)

   
    print(f"Antal personer i datasetet: {induviduals}")

    print(f"Antalet sjuka: {sick_individuals}")

    print("\n------------------------------------------\n")

    print(stats_df_rounded)

    print("\n-------------------------------------------\n")

    print(f"Verklig andel sjukdom: {p_real*100:.2f}%")

    print(f"Simulerad andel sjukdom: {p_sim*100:.2f}%")

    print(f"Skillnad mellan verklig och simulerad: {rel_diff:.2f}%")

    print("\n------------------------------------------\n")

    print("Normalapproximation 95% CI för systoliskt blodtryck")

    
    print("\n------------------------------------------\n")

    print(f"Stickprovsstorlek (n):          {n}")
    print(f"Stickprovsmedelvärde:          {mean_x:.2f}")
    print(f"Stickprovs standardavvikelse:    {s:.2f}")
    print(f"95% konfidensintervall:         {lo:.2f}, {hi:.2f}")

   
    print("\n------------------------------------------\n")

   
   
    print("Bootstrap 95% CI för Systoliskt blodtryck:",(round(float(lower), 1), round(float(upper), 1)))


    
    
    print(f"Standard t-test: T = {t_stat:.3f}, P = {p_val:.4f}")
    print(f"Welch t-test:    T = {t_stat_w:.3f}, P = {p_val_w:.4f}")

    return df

