import pandas as ps
import csv
import plotly.graph_objects as go

df = ps.read_csv("C:/Users/HOME/Downloads/datacsv1.csv")
studentdf = df.loc[df["student_id"]=="TRL_987"]
print(studentdf.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(x = studentdf.groupby("level")["attempt"].mean(),y = ["Level 1","Level 2","Level 3","Level 4"],orientation = "h"))
fig.show()