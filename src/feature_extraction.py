import pandas as pd

df = pd.read_csv("/Users/arnavsharma/Documents/Dev/AI_IT_text_detector/data/raw/data.csv")


print(df.head()) 
print("num samples: ", len(df))
print("label distribution:\n", df['label'].value_counts())

