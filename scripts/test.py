from sklearn.datasets import load_breast_cancer

import pandas as pd

# Load dataset as a pandas DataFrame frame/series pair
cancer_df = load_breast_cancer(as_frame=True)
df = cancer_df.frame

# View the first few rows
print(df.head(50))

