import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.figure_factory as ff

# >> Setup
pd.set_option('mode.chained_assignment', None)


def load_dataset(path):
    return pd.read_excel(path)


seed = 77

data = pd.read_csv("./rotten_tomatoes_movies.csv")

# >> Dash app handler, the variable name must be application
application = dash.Dash(__name__,)

application.title = 'IST-707'
server = application.server

# >> Start drawing
data = data.dropna()
group_labels = data[['audience_rating', 'tomatometer_rating']].columns
fig = ff.create_distplot([data['audience_rating'], data['tomatometer_rating']], group_labels, bin_size=1)

# >> Assign the graph to Dash App handler
application.layout = html.Div(children=[
    html.H4(children='Rotten Tomato - Rating Distribution - Genre'),
    dcc.Graph(id='dist', figure=fig)
])

# >> Program main entrance
if __name__ == '__main__':
    application.run_server(port=8080)
