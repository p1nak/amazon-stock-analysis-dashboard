import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load data
df = pd.read_csv("Amazon.csv")

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create figures
price_fig = px.line(df, x='date', y='close',
                    title="Amazon Closing Price")

volume_fig = px.line(df, x='date', y='volume',
                     title="Trading Volume")

df['daily_return'] = df['close'].pct_change()

return_fig = px.histogram(df, x='daily_return',
                          title="Daily Return Distribution")

# Create dashboard
app = Dash(__name__)

app.layout = html.Div([

    html.H1("Amazon Stock Analysis Dashboard"),

    dcc.Graph(figure=price_fig),

    dcc.Graph(figure=volume_fig),

    dcc.Graph(figure=return_fig)

])

if __name__ == "__main__":
    app.run(debug=True)