import pandas as pd

df = pd.DataFrame({
    "Name" : ["Alice","Bob",None,"David"],
    "Age": [25,None,None,28],
    "Sales": [100,150,270,200]
})

print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())
print(df.isnull().any())

# to remove the empty row , use - drop.na()
df_clean = df.dropna()

print(df_clean)

# to remove empty data from only specific column (in this case Age Column), use= dropna(subset=["Age","Sales"]) 
new_clean = df.dropna(subset=["Age","Sales"])
print(new_clean)

new_data = df
print(new_data)

new_clean = new_data.dropna(axis=1)
print(new_clean)