from dash import dash, html, dcc, Input, Output, State
import pandas as pd
import altair as alt
import dash_bootstrap_components as dbc
alt.data_transformers.enable('default', max_rows=None)

literacy_data = pd.read_csv("../data/processed_data.csv")
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

def plot_altair_line(category):
    filtered_data = literacy_data[literacy_data["category"] == category]
    chart = alt.Chart(filtered_data, title = "Literacy Rate of Age Groups in different grades").mark_line().encode(
        alt.X('attained_grade', title = "Attained Grade"),
        alt.Y('mean(literacy_rate)', title = "Mean Literacy Rate"),
        alt.Color('age_group', title = "Age Group")
    ).properties(
        width=280,
        height=290
    )
    return chart.to_html()

@app.callback(
    Output('rectplot', 'srcDoc'),
    Input('select_grade', 'value'))
def plot_altair_rect(grade):
    filtered_data = literacy_data[literacy_data["attained_grade"] == grade]
    chart = alt.Chart(filtered_data, title = "Literacy Rate in 10 countries for different communities").mark_rect().encode(
        alt.X('country:N', title = "Country"),
        alt.Y('category:N', title = "Category"),
        alt.Color('literacy_rate:Q', title = "Color")
    ).properties(
        width=280,
        height=270
    )
    return chart.to_html()

collapse = html.Div(
    [
        dbc.Button(
            "Learn more",
            id="collapse-button",
            className="mb-3",
            outline=False,
            style={'margin-top': '10px',
                'width': '150px',
                'background-color': 'white',
                'color': 'steelblue'}
        ),
    ]
)

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Row([
            dbc.Col([
                html.H1('Education Attainment Database',
                    style={
                        'color': 'white',
                        'text-align': 'left',
                        'font-size': '48px',  #, 'width': 300}),
                        }),
               dbc.Collapse(
                    html.P("""
                        This dashboard presents information from the fifth release of an international database about education attained from household surveys from around the developing world.""",
                        style={'color': 'white', 'width': '50%'}),
                    id="collapse",
        ),

                    ],
                    md=10),
                dbc.Col([collapse])

                
            ])
        ], style={'backgroundColor': 'steelblue',
                    'border-radius': 3,
                    'padding': 15,
                    'margin-top': 20,
                    'margin-bottom': 20,
                    'margin-right': 15
        })
                    
    ]),
    dbc.Row([
        dbc.Col([
            html.H5('Glossary'),
            html.P('FemRur - Female and Rural'),
            html.P('FemUrb - Female and Urban'),
            html.P('MalRur - Male and Rural'),
            html.P('MalUrb - Male and Urban')
            ],
            md=2,
            style={
                'background-color': '#e6e6e6',
                'padding': 15,
                'border-radius': 3}),
        dbc.Col([
    "Select Category",
    dcc.Dropdown(options = literacy_data["category"].unique(),
        placeholder = "Select a category",
        value = "All",
        id = "select_category"),
        html.Iframe(
            id = 'lineplot',
            srcDoc=plot_altair_line(category="All"),
            style={'border-width': '0', 'width': '100%', 'height': '400px', "overflowY": "show", "overflowX": "show"}),
        ]),
        dbc.Col([
    "Select Grade",
    dcc.Dropdown(options = literacy_data["attained_grade"].unique(),
        placeholder = "Select a grade",
        value = 9,
        id = "select_grade"),
        html.Iframe(
            id = 'rectplot',
            srcDoc=plot_altair_rect(grade=9),
            style={'border-width': '0', 'width': '100%', 'height': '500px', "overflowY": "show", "overflowX": "show"}
            )
        ])
        
        ])
    
    ])
    

@app.callback(
    Output('lineplot', 'srcDoc'),
    Input('select_category', 'value'))
def update_output(category):
    return plot_altair_line(category)

if __name__ == '__main__':
    app.run_server(debug=True)
