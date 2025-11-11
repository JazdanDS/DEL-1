import matplotlib.pyplot as plt

def plots(df):
    plt.figure(figsize=(7,4))
    plt.hist(df["systolic_bp"],bins=20,color="Yellow",edgecolor="black")
    plt.title("Systoliskt blodtryck")
    plt.xlabel("Blodtryck(mmHg)")
    plt.ylabel("Antal personer")
    plt.grid(axis="y",alpha=0.1)
    plt.show()

    plt.figure(figsize=(6,4))
    df.boxplot(column="weight", by="sex", grid=False, patch_artist=True)
    plt.title("Vikt per kön")
    plt.suptitle("")  
    plt.xlabel("Kön")
    plt.ylabel("Vikt (kg)")
    plt.show()
    
    plt.figure(figsize=(6,4))
    df["smoker"].value_counts().sort_index().plot(
        kind="bar", color=["darkgreen", "red"], edgecolor="black"
    )
    plt.title("Andel rökare vs icke-rökare")
    plt.xlabel("Rökare")
    plt.ylabel("Antal personer")
    plt.xticks(rotation=0)
    plt.show()