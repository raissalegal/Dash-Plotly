from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import numpy as np
import plotly.express as px
#import dash_ag_grid as dag

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')



'''
# Plotly graphs
fig = px.histogram(df, x='continent', y='pop', histfunc='avg')
'''

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My App from Plotly Dash Course'),
    html.Hr(),
    dcc.Dropdown(
        options = pd.unique(df["brand"]),
        value = 'Revlon', id='brand-dropdown',
        placeholder = "Select a brand"
    ),
    html.Hr(),
    dcc.RadioItems(
        #options = np.sort(pd.unique(df["group"]))
        options={
        0: "Fenty Beauty's PRO FILT'R Foundation Only",
        1: "Make Up For Ever's Ultra HD Foundation Only",
        2: "US Best Sellers",
        3: "BIPOC-recommended Brands with BIPOC Founders",
        4: "BIPOC-recommended Brands with White Founders",
        5: "Nigerian Best Sellers",
        6: "Japanese Best Sellers",
        7: "Indian Best Sellers"
        }
    )

    #dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='column-options'),
    #dag.AgGrid(
    #   id="grid",
    #   rowData=df.to_dict("records"),
    #   columnDefs=[{"field": i} for i in df.columns],
    #),
    #dcc.Graph(figure=fig, id='graph1')
])
'''
# Add controls to build the interaction
@callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id='column-options', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig
'''

# Run the app
if __name__ == '__main__':
    app.run(debug=True)