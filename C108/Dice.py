import random
import plotly_express as px
import plotly.figure_factory as pf

count = []
diceResult = []

for i in range(0,100):
    dice1 = random.randint(1,6)
    print(dice1)

    dice2 = random.randint(1,6)
    print(dice2)

    diceResult.append(dice1+dice2)
    count.append(i)

fig = pf.create_distplot([diceResult],["Results"],show_hist=False)
fig.show()