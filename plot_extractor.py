import pandas as pd
import re

dataset_name = "wiki_movie_plots_deduped.csv"
column_name = "Plot"
no_of_rows = 200

def format_text(text):
    '''Formats text by removing citations and also unicode and newline characters'''
    citations = r'\[[0-9]*\]'
    regex1 = r'\''
    regex2 = r'\n'
    regex3 = r'\r'
    #text = re.sub(r'\[[0-9]*\]', ' ', text) Removes the citations and square brackets
    text = re.sub(regex1, "'", text)
    text = re.sub("|".join([citations, regex2, regex3]) , "", text)
    text = text.encode("ascii","ignore").decode('UTF-8') #Removing unicode characters & converting bytes to string
    text = "<BOL>" + str(text) + "<EOL>\n\n"
    return text


df = pd.read_csv(dataset_name)

#Applying conditions to Dataframe
df = df.loc[df["Origin/Ethnicity"] == "American"].tail(no_of_rows)

#Extracting plots to plots.txt
with open("plots.txt", "a") as file:
    for i in range(no_of_rows):
        raw_data = df[column_name].iloc[i]
        plot = format_text(raw_data)
        file.write(plot)