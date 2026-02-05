import pandas as pd

print("Starting preprocessing...")

df = pd.read_csv("dataset.csv")
print("Dataset loaded")

disease_col = "diseases"
symptom_columns = df.columns.drop(disease_col)

print("Processing symptoms... please wait")

# Vectorized conversion (FAST)
df["symptoms_text"] = (
    df[symptom_columns]
    .apply(lambda row: " ".join(symptom.replace("_", " ")
    for symptom, val in row.items() if val == 1), axis=1)
)

processed_df = df[["symptoms_text", disease_col]]
processed_df.columns = ["symptoms_text", "disease"]

processed_df.to_csv("processed_dataset.csv", index=False)

print("✅ Dataset preprocessed successfully")

