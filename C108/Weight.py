import plotly.figure_factory as pf
import csv
import pandas as pd

data = pd.read_csv("Distribution.csv")

mean = data["Weight(Pounds)"]/2
print(mean)

fig = pf.create_distplot([mean.tolist()],["Weight in pounds"],show_hist=False)
fig.show()
