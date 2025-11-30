import pandas as pd
#Läser in datasetet

def load_csv(filepath):
    with open(filepath, "r",encoding="utf-8") as f:
        df = pd.read_csv(f)
        
        return(df)

#Rensar och den data som vi läst in
#Tar bort whitespace
#Standardiser sex och smoker
#Gör om värden som skall vara numeriska till numeriska
#Dropna på rader som saknar värden i de kolumer vi vill ha

def clean_df(df):
    df.columns = [i.strip() for i in df.columns]
    df["sex"] = df["sex"].astype(str).str.strip().str.upper()
    df["smoker"] = df["smoker"].astype(str).str.strip().str.capitalize()
    df["cholesterol"] = pd.to_numeric(df["cholesterol"],errors="coerce")
    df["disease"] = pd.to_numeric(df["disease"],errors="coerce")
    df["age"] = pd.to_numeric(df["age"], errors="coerce").astype(int)
    df = df.dropna(subset=["weight","height","systolic_bp","cholesterol","disease","age"])
    df["disease"] = df["disease"].astype(int)
   
    return df

#Asisterande funktion som både läser och rensar datan för att underlätta

def load_and_clean(filepath):
    df = load_csv(filepath)
    df = clean_df(df)
    
    return df

