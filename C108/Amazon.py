import plotly.figure_factory as pf
import pandas as pd
import csv
import plotly_express as px

data = pd.read_csv("AmazonProducts.csv")

#mean = data["Avg Rating"]/2
#print(mean)

fig = pf.create_distplot([data["Avg Rating"].tolist()],["Average Rating"])
fig.show()