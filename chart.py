import plotly.offline as poff
import plotly.tools as tls
import plotly.graph_objs as go

import pandas as pd


df = pd.read_csv("t1.csv")

x1=df.timeS
y1=df.x
x2=df.timeS
y2=df.y
x3=[300, 400, 500]
y3=[600, 700, 800]
x4=[4000, 5000, 6000]
y4=[7000, 8000, 9000]

fig = tls.make_subplots(rows=2, cols=2,vertical_spacing=0.1,horizontal_spacing=0.01, print_grid=True)

fig.append_trace(go.Scatter({'x':x1, 'y':y2, 'name':'A1'},), 1, 1)
fig.append_trace(go.Scatter({'x':x2, 'y':y2, 'name':'B2'},), 2, 2)
fig.append_trace(go.Scatter({'x':x3, 'y':y3, 'name':'A2'},), 2, 1)
fig.append_trace(go.Scatter({'x':x4, 'y':y4, 'name':'B1'},), 1, 2)

fig['layout'].update(title='Multiple Subplots')
url = poff.plot(fig, filename="test23.html")