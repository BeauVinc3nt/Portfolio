import pandas as pd

# READING CSV FILE WITH FOUND SQUIRREL DATA TO EXTRAPOLATE:
data = pd.read_csv("./Squirrels data set/2018_Central_Park_Squirrel_Data.csv")   

# IDENTIFYING AND ASSIGNING COLORS TO THE DIFFERENT SQUIRREL COLORS IN DATA SET.
grey_squirrels = data[data["Primary Fur Color"] == "Gray"] # In dataset where Primary fur colour column = colour X
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

# SQUIRREL COLOUR COUNTS:
Gray_Squirrels_count = len(grey_squirrels)  # Gets the length of rows for squirrels to find how many there are.
Red_Squirrels_count = len(red_squirrels)
Black_Squirrels_count = len(black_squirrels)

# SETTING UP A DICTIONARY FORMAT TAKING IN 2 PARAMS
data_dictionary = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray_Squirrels_count, Red_Squirrels_count, Black_Squirrels_count]
}

# Converting dictionary into a Dataframe to make a structured table.
Squirrels_data_df = pd.DataFrame(data_dictionary)
Squirrels_data_df.to_csv("./Squirrels data set/Squirrel_counts.csv")
