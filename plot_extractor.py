import pandas as pd

dataset_name = "wiki_movie_plots_deduped.csv"
column_name = "Plot"
no_of_rows = 200

df = pd.read_csv(dataset_name)

#Applying conditions to Dataframe
df = df.loc[df["Origin/Ethnicity"] == "American"].tail(no_of_rows)

#Extracting plots to plots.txt
with open("plots.txt", "a") as file:
    for i in range(no_of_rows):
        data = "<BOL>"+str(df[column_name].iloc[i].encode("ascii","ignore"))+"<EOL>\n\n" #ignoring unicode characters
        file.write(data)