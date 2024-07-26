import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_count = data["Primary Fur Color"].value_counts()
color_count.index.name = "Fur Color"
color_count.name = "Count"
color_count.to_csv("squirrel_count.csv")
