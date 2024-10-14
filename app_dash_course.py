from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

fig = px.scatter(
    df, x="V", y="S",
    hover_data=['H',"S","V","L","hex"]
    )

columnDefs = [
    { 'field': 'brand'},
    { 'field': 'brand_short'},
    { 'field': 'product'},
    { 'field': 'product_short'},
    { 'field': 'hex'},
    { 'field': 'H'},
    { 'field': 'S'},
    { 'field': 'V'},
    { 'field': 'L'},
    { 'field': 'group'},
]

grid = dag.AgGrid(
    id="df_aggrid",
    rowData=df.to_dict("records"),
    columnDefs=columnDefs,
    dashGridOptions={'pagination':True},
    className="ag-theme-alpine-dark",
    columnSize="sizeToFit",
)

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
    ),
    html.Hr(),
    
    dcc.RangeSlider(
        df['S'].min(),
        df['S'].max(),
        step=0.05,
    ),
    html.Hr(),
    
    dcc.Input(
        placeholder='Enter a value...',
        type='number',
        value='',
    ),
    html.Hr(),

    dcc.Graph(figure=fig, id='scatter_plot'),
    html.Hr(),
    
    
    grid

])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)