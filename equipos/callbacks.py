
# Dash components, html, and dash tables
from dash.dependencies import Input, Output

# Custom dependencies
from app import app
import commons.functions as f
import commons.data as d
from equipos.specs import object_specs


for fun in f.create_callback_functions_from_specs(object_specs=object_specs):
    exec(fun, locals())



'''
@app.callback(
    Output('lov_team', 'options'),
    [Input('lov_majorLeague', 'value'), Input('lov_season', 'value') ]
    )
def set_team_from_majorleague(lov_majorLeagueId=None, lov_seasonId=None):
    filter_cols = { 'majorLeagueId' : lov_majorLeagueId,
              'seasonId' : lov_seasonId
            }

    df = f.filter_df( df = es.object_specs['lov_team']['dataset'], filter_cols=filter_cols)

    lov = f.create_list_of_values( df, label_col = es.object_specs['lov_team']['label_col'],  value_col = es.object_specs['lov_team']['value_col'] )

    return lov
'''
