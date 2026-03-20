import pandas as pd

df = pd.read_csv("../dataset/tickets.csv")

df["text"] = (
    df["ticket_subject"] + " " +
    df["ticket_description"] + " " +
    df["subcategory"].astype(str) + " " +
    df["device_type"].astype(str) + " " +
    df["tags"].astype(str)
)

df = df[["text","category"]]

df = df.dropna()

df["text"] = df["text"].str.lower()

df.to_csv("../dataset/cleaned_tickets.csv", index=False)

print("Dataset cleaned successfully")