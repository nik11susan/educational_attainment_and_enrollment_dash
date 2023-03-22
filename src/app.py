from dash import dash, html, dcc
import pandas as pd
import altair as alt

literacy_data = pd.read_csv("../data/processed_data.csv")
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

chart = alt.Chart(literacy_data).mark_line().encode(
    x='attained_grade',
    y='mean(All)',
    color='age_group'
)

app.layout = html.Div([
    "Select Country",
    dcc.Dropdown(options = literacy_data["country"].unique(),
        value = "India",
        multi = True,
        placeholder = "Select a country",
        id = "select_country"),
        html.Iframe(
            srcDoc=chart.to_html(),
            style={'border-width': '0', 'width': '100%', 'height': '400px'})
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
