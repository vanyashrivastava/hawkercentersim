import matplotlib.pyplot as plt
import pandas as pd


def show_kpi_dashboard():
    df = pd.DataFrame({
        "Layout": ["A", "B", "C", "D"],
        "Avg Prep Time (s)": [12, 8, 15, 11],
        "Avg Steps": [30, 18, 42, 27],
        "Success Rate (%)": [80, 95, 65, 85],
        "Stove Wait Time": [6, 3, 10, 5]
    })

    print(df)  

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("HawkerBotSim Layout KPI Dashboard", fontsize=16)

    axes[0, 0].bar(df["Layout"], df["Avg Prep Time (s)"], color="skyblue")
    axes[0, 0].set_title("Avg Prep Time")
    axes[0, 0].set_ylabel("Seconds")

    axes[0, 1].bar(df["Layout"], df["Avg Steps"], color="orange")
    axes[0, 1].set_title("Avg Agent Steps")
    axes[0, 1].set_ylabel("Steps")

    axes[1, 0].bar(df["Layout"], df["Success Rate (%)"], color="green")
    axes[1, 0].set_title("Success Rate")
    axes[1, 0].set_ylabel("%")

    axes[1, 1].bar(df["Layout"], df["Stove Wait Time"], color="red")
    axes[1, 1].set_title("Stove Wait Time")
    axes[1, 1].set_ylabel("Steps")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
