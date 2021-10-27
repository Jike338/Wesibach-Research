import pandas as pd

# to read data in a single excel file
new_csv = pd.read_csv("test.csv")
new_csv = new_csv['descriptions']

for line in new_csv:
    print(line)
