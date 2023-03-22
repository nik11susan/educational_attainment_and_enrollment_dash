from dash import dash, html, dcc
import pandas as pd
import altair as alt

literacy_data = pd.read_csv("../data/processed_data.csv")
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

def plot_altair(category):
    chart = alt.Chart(literacy_data).mark_line().encode(
        x='attained_grade',
        y='mean(category)',
        color='age_group'
    )
    return chart.to_html()

app.layout = html.Div([
    "Select Country",
    dcc.Dropdown(options = literacy_data["category"].unique(),
        multi = True,
        placeholder = "Select a category",
        id = "select_category"),
        html.Iframe(
            id = 'lineplot',
            srcDoc=plot_altair(category="All"),
            style={'border-width': '0', 'width': '100%', 'height': '400px'})
    ])

@app.callback(
    Output('lineplot', 'srcDoc'),
    Input('select_category', 'value'))
def update_output(category):
    return plot_altair(category)

if __name__ == '__main__':
    app.run_server(debug=True)
