import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src import Metrics as M

def plots(df):
    sns.set(style="whitegrid")

    plt.figure(figsize=(7,4))
    sns.histplot(df["systolic_bp"],bins=20,color="Yellow",edgecolor="black")
    plt.title("Systoliskt blodtryck")
    plt.xlabel("Blodtryck(mmHg)")
    plt.ylabel("Antal personer")
    plt.grid(axis="y",alpha=0.3)
    plt.show()
    plt.close()

    plt.figure(figsize=(6,4))
    sns.boxplot(data=df, y="weight",x="sex",hue="sex", palette="Set2",legend=False)
    plt.title("Vikt per kön")
    plt.suptitle("")  
    plt.xlabel("Kön")
    plt.ylabel("Vikt (kg)")
    plt.show()
    plt.close()
    
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x="smoker", hue="smoker", palette=["green", "red"], legend=False)
    plt.title("Andel rökare vs icke-rökare")
    plt.xlabel("Rökare")
    plt.ylabel("Antal personer")
    plt.show()
    plt.close()
    
    lower, upper, boot_means = M.bootstrap(df,B=3000)
    plt.hist(boot_means,bins=50, color="skyblue", edgecolor="black")
    plt.axvline(lower, color="red", linestyle="--", label="Nedre CI-gräns")
    plt.axvline(upper, color="red", linestyle="--", label="Övre CI-gräns")
    plt.axvline(np.mean(boot_means), color="black", linestyle="--", label="Bootstrap-medel")

    plt.title("Bootstrapfördelning av medelvärden för Systolisk blodtryck")
    plt.xlabel("Medelvärde")
    plt.ylabel("Antal")
    plt.legend()
    plt.show()
    plt.close()