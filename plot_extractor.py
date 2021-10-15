import pandas as pd
import re

dataset_name = "wiki_movie_plots_deduped.csv"
column_name = "Plot"
#no_of_rows = 200

def format_text(text):
    '''Formats text by removing citations and also unicode & newline characters'''
    citations = r'\[[0-9]*\]'
    regex1 = r'\''
    regex2 = r'\n' #line feed
    regex3 = r'\r' #carriage return

    text = re.sub(regex1, "'", text) #replaces \'s with 's
    text = re.sub("|".join([citations, regex2, regex3]) , "", text) #removes regex patterns from text
    text = text.encode("ascii","ignore").decode('UTF-8') #removes unicode characters & converting bytes to string
    text = "<|startoftext|>" + str(text) + "<|endoftext|>\n\n"
    return text


df = pd.read_csv(dataset_name)

#Applying conditions to Dataframe
df = df.loc[df["Origin/Ethnicity"] == "American"]#.tail(no_of_rows)

#Extracting plots to plots.txt
with open("plots.txt", "a") as file:
    for i in range(df.shape[0]):
        raw_data = df[column_name].iloc[i]
        plot = format_text(raw_data)
        file.write(plot)