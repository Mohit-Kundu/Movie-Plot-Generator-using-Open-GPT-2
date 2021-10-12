import pandas as pd

dataset_name = "wiki_movie_plots_deduped.csv"
column_name = "Plot"

df = pd.read_csv(dataset_name)

#Applying conditions to Dataframe
df = df.loc[df["Origin/Ethnicity"] == "American"]

#Extracting plots to plots.txt
with open("plots.txt", "a") as file:
    for i in range(500):
        data = "<BOL>"+str(df[column_name].iloc[i].encode("ascii","ignore"))+"<EOL>\n\n"
        file.write(data)