import random
import plotly.figure_factory as pf
import pandas as pd

data = pd.read_csv("Distribution.csv")

#index = data.pop("Index")
mean = data["Height(Inches)"]/2
print(mean)

fig = pf.create_distplot([mean.tolist()],["Height in inches"],show_hist=False)
fig.show()
