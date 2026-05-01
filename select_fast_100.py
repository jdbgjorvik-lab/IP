import pandas as pd

df = pd.read_csv("scan_result.csv")

df = df.dropna()
df = df.sort_values("latency")

top100 = df.head(100)

with open("fast_100.txt", "w") as f:
    for _, r in top100.iterrows():
        f.write(f"{r['ip']}:443#FAST\n")

print("Top 100 generated")