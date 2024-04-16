import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

df = pd.DataFrame({'Net': [15,20,20,-15], 'Date' : ['1', '1', '2', '2']})
print(df)
fig = px.bar(df, x='Date', y='Net')
plot(fig, auto_open=True)

