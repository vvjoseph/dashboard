import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

colors = {
    'background': '#008000',
    'text': '#FFFFFF',
    'align': 'center'
}


index_page = html.Div(children=[
    html.H1(
        children='Precision Agriculture for Development',
        style={
            'textAlign': colors['align'],
            'backgroundColor': colors['background'],
            'color': colors['text'],
            #'font-family': 'Arial, Helvetica, sans-serif'
            }
    ),
    html.Div([
##        html.Div([
##            html.Img(src='/assets/dash_template.png'),
##            ],className="three columns", style={'height':'100px',}),
        html.Div([                       
            ],style={'padding':20}),        
        html.Div([
            dcc.Link(html.Button('Pest Helpline'), href='/pest'),
            html.Br(),
            ],style={'padding':20}),
        html.Div([        
            dcc.Link(html.Button('Inbound Usage'), href='/inbound'),
            html.Br(),
            ],style={'padding':20}),
        html.Div([                
            dcc.Link(html.Button('Outbound Usage'), href='/outbound'),
            html.Br(),
            ],style={'padding':20}),       
        html.Div([                       
            dcc.Link(html.Button('Farmer Profiles'), href='/profiles'),
            html.Br(),
            ],style={'padding':20}),
        html.Div([                               
            dcc.Link(html.Button('Training'), href='/training'),
            html.Br(),
            ],style={'padding':20}),
        html.Div([                                      
            dcc.Link(html.Button('Polling'), href='/polling'),
            html.Br(),
            ],style={'padding':20}),        
    ], style={'textAlign': 'center'}),
    
], style={'height':'600px', 'textAlign': 'center', 'background-image': 'url(/assets/pic_new.png)', 'background-repeat':'no-repeat'})



###table
##def generate_table(dataframe, max_rows=15):
##    return html.Table(
##        # Header
##        [html.Tr([html.Th(col) for col in dataframe.columns])] +
##
##        # Body
##        [html.Tr([
##            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
##        ]) for i in range(min(len(dataframe), max_rows))]
##    )
##
##
###pest
##
##df_pest_1 = pd.read_csv(
##    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/total_questions.csv')
##
##df_pest_2 = pd.read_csv(
##    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/district_block.csv')
##
##df_pest_names = df_pest_2.drop(['block'], axis=1)
##column = list(df_pest_names.columns.values)
##
##traces = []
##for col in column:
##    #df_by_pest = df_pest_2[df_pest_2['continent'] == i]
##    df_check = df_pest_2.filter(items=['block',col])
##    df_check = df_check[df_check[col] != 0]
##    df_check = df_check.sort_values([col], ascending=0)
##    traces.append(go.Bar(
##        x=df_check['block'],
##        y=df_check[col],
##        #text=df_by_continent['country'],
##        #mode='markers',
##        #opacity=0.7,
##        #marker={
##         #   'size': 15,
##        #    'line': {'width': 0.5, 'color': 'white'}
##        #},
##        name=col
##    ))
##
##
##pest_layout = html.Div(style={'backgroundColor': colors['background']}, children=[
##    html.H1(
##        children='dashPAD',
##        style={
##            'textAlign': 'center',
##            'color': colors['text']
##            }
##    ),
##
##    html.Div([ 
##    dcc.Graph(
##        id='pest_1',
##        figure={
##            'data': [
##                  go.Bar(
##                      x=df_pest_1['Pest'],
##                      y=df_pest_1['Count'],
##                    ) 
##                
##            ],
##            'layout': go.Layout(
##                title='Frequency of pest incidence',
##                xaxis={'title': 'Pest'},
##                yaxis={'title': 'No. of questions'},
##                #margin=dict(t=50),
##                hovermode='closest'
##            )
##        }
##    ),
##    ],style={'padding': 100}),
##
##    html.Div([ 
##    dcc.Graph(
##        id='pest_2',
##        figure={
##            'data': traces,
##            'layout': go.Layout(
##                title='Pest incidence by blocks',
##                barmode='group',
##                xaxis={'title': 'Blocks'},
##                yaxis={'title': 'No. of questions'},
##                hovermode='closest'
##            )
##        }
##    ),
##    ],style={'padding': 100}),
##    
##    dcc.Link('Usage', href='/usage'),
##    html.Br(),
##    dcc.Link('Index', href='/'),
##
##])




##############     pest     ##################


df_pest1 = pd.read_csv(
    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/pest_dash_final.csv')
df_pest2 = pd.read_csv(
    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/pest_dash_district_final.csv')
df_pest3 = pd.read_csv(
    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/pest_dash_spatial_final.csv')

dropped_pest = df_pest1.drop(['month_week','crop'], axis=1)
metrics_pest =  list(dropped_pest.columns.values)
#crops =  ['paddy', 'tomato', 'brinjal']
crops = df_pest1['crop'].unique()
districts_pest = df_pest2['district'].unique()
weeks_pest = df_pest1['month_week'].unique()

pest_layout = html.Div(children=[
##    html.H1(
##        children='Precision Agriculture for Development',
##        style={
##            'textAlign': colors['align'],
##            'backgroundColor': colors['background'],
##            'color': colors['text']
##            }
##    ),

    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='crop',
                    options=[{'label': i, 'value': i} for i in crops],
                    value='paddy'
                ),
                dcc.Dropdown(
                    id='metric-pest',
                    options=[{'label': i, 'value': i} for i in metrics_pest],
                    value='blb'
                ),
                dcc.Graph(id='graph-1-pest'),
                dcc.Dropdown(
                    id='district-pest',
                    options=[{'label': i, 'value': i} for i in districts_pest],
                    value='BALANGIR'
                ),
                dcc.Graph(id='graph-2-pest'),    
            ]),

        ], className="six columns"),
        

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='week-metric-pest',
                    options=[{'label': i, 'value': i} for i in weeks_pest],
                    value='Oct-Week 4'
                ),
                dcc.Graph(id='graph-4-pest'),
                dcc.Graph(id='graph-3-pest'),
            ]),
        ], className="six columns"),

    ], className="row")

])


@app.callback(
    dash.dependencies.Output('graph-1-pest', 'figure'),
    [dash.dependencies.Input('metric-pest', 'value'),
     dash.dependencies.Input('crop', 'value')])

def update_graph_1(metric,crop):
    filtered = df_pest1[df_pest1['crop'] == crop]
    filtered = filtered[(filtered[[metric]] != 0).all(axis=1)]   
    return {
        'data': [go.Scatter(
            x=filtered['month_week'],
            y=filtered[metric],
        )],
        'layout': go.Layout(
            height=250,
##            xaxis={
##                'title': 'Week',
##            },
##            yaxis={
##                'title': 'No. of questions',
##            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('graph-2-pest', 'figure'),
    [dash.dependencies.Input('metric-pest', 'value'),
     dash.dependencies.Input('crop', 'value'),
     dash.dependencies.Input('district-pest', 'value')])

def update_graph_2(metric,crop,district):

    filtered_dist = df_pest2[df_pest2['district'] == district]
    filtered_dist = filtered_dist[filtered_dist['crop'] == crop]
    filtered_dist = filtered_dist[(filtered_dist[[metric]] != 0).all(axis=1)]   

 
    return {
        'data': [go.Scatter(
            x=filtered_dist['month_week'],
            y=filtered_dist[metric],
        )],
        'layout': go.Layout(
            height=250,
##            xaxis={
##                'title': 'Week',
##            },
##            yaxis={
##                'title': 'No. of questions',
##            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('graph-3-pest', 'figure'),
    [dash.dependencies.Input('metric-pest', 'value'),
     dash.dependencies.Input('crop', 'value'),
     dash.dependencies.Input('district-pest', 'value'),
     dash.dependencies.Input('week-metric-pest', 'value')])

def update_graph_3(metric,crop,district,week):

    filtered_dist_block = df_pest3[df_pest3['district'] == district]
    filtered_dist_block = filtered_dist_block[filtered_dist_block['crop'] == crop]
    filtered_dist_block = filtered_dist_block[filtered_dist_block['month_week'] == week]
    filtered_dist_block = filtered_dist_block[(filtered_dist_block[[metric]] != 0).all(axis=1)]
    filtered_dist_block = filtered_dist_block.sort_values([metric], ascending=0)    
    
    return {
        'data': [go.Bar(
            x=filtered_dist_block['block'],
            y=filtered_dist_block[metric],
        )],
        'layout': go.Layout(
            height=300,
            bargap=0.9,
##            xaxis={
##                'title': 'Blocks',
##            },
##            yaxis={
##                'title': 'No. of questions',
##            },
            margin={'l': 0, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('graph-4-pest', 'figure'),
    [dash.dependencies.Input('metric-pest', 'value'),
     dash.dependencies.Input('crop', 'value'),
     dash.dependencies.Input('week-metric-pest', 'value')])

def update_graph_4(metric,crop,week):

    filtered_block = df_pest3[df_pest3['month_week'] == week]
    filtered_block = filtered_block[filtered_block['crop'] == crop]
    filtered_block = filtered_block[(filtered_block[[metric]] != 0).all(axis=1)]
    filtered_block = filtered_block.sort_values([metric], ascending=0)    
    
    return {
        'data': [go.Bar(
            x=filtered_block['block'],
            y=filtered_block[metric],
        )],
        'layout': go.Layout(
            height=250,
            bargap=0.5,
##            xaxis={
##                'title': 'Blocks',
##            },
##            yaxis={
##                'title': 'No. of questions',
##            },
            margin={'l': 0, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }






##############     inbound      ##################


df_in1 = pd.read_csv(
    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/inbound_dash_final.csv')
df_in2 = pd.read_csv(
    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/inbound_dash_district_final.csv')
df_in3 = pd.read_csv(
    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/inbound_dash_spatial_final.csv')

dropped = df_in1.drop(['month','month_week'], axis=1)
metrics = list(dropped.columns.values)
districts = df_in2['district'].unique()
weeks = df_in2['month_week'].unique()


##sections = df_in1.drop(['month','month_week','Total_inbound_calls','Total_unique_callers','Average_duration'], axis=1)
##hits = list(sections.columns.values)
##
####traces = []
####for col in hits:
####    traces.append(go.Scatter(
####        x=df_in1['month_week'],
####        y=df_in1[col],
##        mode='lines+markers',
##        #text=df_by_continent['country'],
##        #mode='markers',
##        #opacity=0.7,
##        #marker={
##         #   'size': 15,
##        #    'line': {'width': 0.5, 'color': 'white'}
##        #},
##        name=col
##    ))
##

inbound_layout = html.Div(children=[
##    html.H1(
##        children='dashPAD',
##        style={
##            'textAlign': colors['align'],
##            'backgroundColor': colors['background'],
##            'color': colors['text']
##            }
##    ),
    
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='metric',
                    options=[{'label': i, 'value': i} for i in metrics],
                    value='Total_inbound_calls',
                ),

                dcc.Graph(id='graph-1'),
##                dcc.Graph(
##                    id='test',
##                    figure={
##                        'data': traces,
##                        'layout': go.Layout(
##                            height=500,
####                            title='Pest incidence by blocks',
####                            barmode='group',
####                            xaxis={'title': 'Blocks'},
####                            yaxis={'title': 'No. of questions'},
##                            margin={'l': 40, 't': 10, 'r': 0},
##                            hovermode='closest'
##                        )
##                    }
##                ),

            ]),

        ], className="six columns"),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='district',
                    options=[{'label': i, 'value': i} for i in districts],
                    value='BALANGIR'
                ),
                dcc.Graph(id='graph-2'),    
                dcc.Dropdown(
                    id='week',
                    options=[{'label': i, 'value': i} for i in weeks],
                    value='Oct-Week 2'
                ),
                dcc.Graph(id='graph-3'),
            ]),
        ], className="six columns"),

    ], className="row")

])


###style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}
##    html.Div([
##    dcc.Graph(
##        id='inbound_1',
##        figure={
##            'data': [
##                  go.Bar(
##                      x=df_in1['Section'],
##                      y=df_in1['Frequency'],
##                    ) 
##                
##            ],
##            'layout': go.Layout(
##                title='Sectionwise hits',
##                xaxis={'title': 'Section'},
##                yaxis={'title': 'Frequency'},
##                hovermode='closest'
##            )
##        }
##    ),
##    ],style={'padding': 100}),
##
##    html.Div([
##    dcc.Graph(
##        id='inbound_2',
##        figure={
##            'data': [
##                  go.Bar(
##                      x=df_in2['Section'],
##                      y=df_in2['%'],
##                    ) 
##                
##            ],
##            'layout': go.Layout(
##                title='Sections vs % of farmers who visited atleast once',
##                xaxis={'title': 'Section'},
##                yaxis={'title': '% of farmers visited atleast once'},
##                hovermode='closest'
##            )
##        }
##    ),
##    ],style={'padding': 100}),
##
##    html.Div([    
##    dcc.Graph(
##        id='inbound_3',
##        figure={
##            'data': [
##                  go.Scatter(
##                      x=df_in3['month'],
##                      y=df_in3['n()'],
##                    ) 
##                
##            ],
##            'layout': go.Layout(
##                title='Total inbound calls by month',
##                xaxis={'title': 'Month'},
##                yaxis={'title': 'Total no. of calls'},
##                hovermode='closest'
##            )
##        }
##    ),
##    ],style={'padding': 100}),
##
##    dcc.Link('Pest', href='/pest'),
##    html.Br(),
##    dcc.Link('Index', href='/'),
    

@app.callback(
    dash.dependencies.Output('graph-1', 'figure'),
    [dash.dependencies.Input('metric', 'value')])

def update_graph_1(metric):

    filtered = df_in1[(df_in1[[metric]] != 0).all(axis=1)]
    
    return {
        'data': [go.Scatter(
            x=filtered['month_week'],
            y=filtered[metric],
            mode='lines+markers',
            )],
        'layout': go.Layout(
            height=500,
##            xaxis={
##                'title': 'Week',
##            },
##            yaxis={
##                'title': metric,
##            },
            margin={'l': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('graph-2', 'figure'),
    [dash.dependencies.Input('metric', 'value'),
     dash.dependencies.Input('district', 'value')])

def update_graph_2(metric,district):

    filtered_dist = df_in2[df_in2['district'] == district]
    filtered_dist = filtered_dist[(filtered_dist[[metric]] != 0).all(axis=1)]
    
    return {
        'data': [go.Scatter(
            x=filtered_dist['month_week'],
            y=filtered_dist[metric],
        )],
        'layout': go.Layout(
            height=250,
##            xaxis={
##                'title': 'Week',
##            },
##            yaxis={
##                'title': metric,
##            },
            margin={'l': 0, 'b': 100, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('graph-3', 'figure'),
    [dash.dependencies.Input('metric', 'value'),
     dash.dependencies.Input('district', 'value'),
     dash.dependencies.Input('week', 'value')])

def update_graph_3(metric,district,week):

    filtered_dist_block = df_in3[df_in3['district'] == district]
    filtered_dist_block = filtered_dist_block[filtered_dist_block['month_week'] == week]
    filtered_dist_block = filtered_dist_block[(filtered_dist_block[[metric]] != 0).all(axis=1)]
    filtered_dist_block = filtered_dist_block.sort_values([metric], ascending=0)    
    
    return {
        'data': [go.Bar(
            x=filtered_dist_block['block'],
            y=filtered_dist_block[metric],
        )],
        'layout': go.Layout(
            height=250,
##            xaxis={
##                'title': 'Blocks',
##            },
##            yaxis={
##                'title': metric,
##            },
            margin={'l': 0, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }



                          
    
     
                          
        
##############     outbound      ##################


df_out1 = pd.read_csv(
    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/outbound_dash_final.csv')
df_out2 = pd.read_csv(
    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/outbound_dash_district_final.csv')
df_out3 = pd.read_csv(
    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/outbound_dash_spatial_final.csv')

dropped_out = df_out1.drop(['month','month_week'], axis=1)
metrics_out =  list(dropped_out.columns.values)
districts_out = df_out2['district'].unique()
weeks_out = df_out2['month_week'].unique()


outbound_layout = html.Div(children=[
##    html.H1(
##        children='dashPAD',
##        style={
##            'textAlign': colors['align'],
##            'backgroundColor': colors['background'],
##            'color': colors['text']
##            }
##    ),
##    
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='metric-out',
                    options=[{'label': i, 'value': i} for i in metrics_out],
                    value='Total_outbound_calls'
                ),

                dcc.Graph(id='graph-1-out'),

            ]),

    ], className="six columns"),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='district-out',
                    options=[{'label': i, 'value': i} for i in districts_out],
                    value='BALANGIR'
                ),
                dcc.Graph(id='graph-2-out'),
                dcc.Dropdown(
                    id='week-out',
                    options=[{'label': i, 'value': i} for i in weeks_out],
                    value='Oct-Week 2'
                ),

                dcc.Graph(id='graph-3-out'),
            ]),
        ], className="six columns"),

    ], className="row")

])


@app.callback(
    dash.dependencies.Output('graph-1-out', 'figure'),
    [dash.dependencies.Input('metric-out', 'value')])

def update_graph_1(metric):

    filtered = df_out1[(df_out1[[metric]] != 0).all(axis=1)]
    
    return {
        'data': [go.Scatter(
            x=filtered['month_week'],
            y=filtered[metric],
        )],
        'layout': go.Layout(
            height=500,
##            xaxis={
##                'title': 'Week',
##            },
##            yaxis={
##                'title': metric,
##            },
            margin={'l': 40, 'b': 100, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('graph-2-out', 'figure'),
    [dash.dependencies.Input('metric-out', 'value'),
     dash.dependencies.Input('district-out', 'value')])

def update_graph_2(metric,district):

    filtered_dist = df_out2[df_out2['district'] == district]
    filtered_dist = filtered_dist[(filtered_dist[[metric]] != 0).all(axis=1)]
    
    return {
        'data': [go.Scatter(
            x=filtered_dist['month_week'],
            y=filtered_dist[metric],
        )],
        'layout': go.Layout(
            height=250,
##            xaxis={
##                'title': 'Week',
##            },
##            yaxis={
##                'title': metric,
##            },
            margin={'l': 0, 'b': 100, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('graph-3-out', 'figure'),
    [dash.dependencies.Input('metric-out', 'value'),
     dash.dependencies.Input('district-out', 'value'),
     dash.dependencies.Input('week-out', 'value')])

def update_graph_3(metric,district,week):

    filtered_dist_block = df_out3[df_out3['district'] == district]
    filtered_dist_block = filtered_dist_block[filtered_dist_block['month_week'] == week]
    filtered_dist_block = filtered_dist_block[(filtered_dist_block[[metric]] != 0).all(axis=1)]
    filtered_dist_block = filtered_dist_block.sort_values([metric], ascending=0)    
    
    return {
        'data': [go.Bar(
            x=filtered_dist_block['block'],
            y=filtered_dist_block[metric],
        )],
        'layout': go.Layout(
            height=250,
##            xaxis={
##                'title': 'Blocks',
##            },
##            yaxis={
##                'title': metric,
##            },
            margin={'l': 0, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }





        


                          
                    
























                          
 

#### outbound usage
##
##df_table_out = pd.read_csv(
##    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/report_out.csv')
##
##df_out1 = pd.read_csv(
##    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/by_dist.csv')
##
##
##traces_out = []
###columns = df_out1['district'].tolist()
##for dist in df_out1.district.unique():
##    df_by_dist = df_out1[df_out1['district'] == dist]
##    #df_check = df_pest_2.filter(items=['combined',col])
##    #df_check = df_check[df_check[col] != 0]
##    #df_check = df_check.sort_values([col], ascending=0)
##    traces_out.append(go.Scatter(
##        x=df_by_dist['n().x'],
##        y=df_by_dist['n().y'],
##        text=df_by_dist['block'],
##        mode='markers',
##        opacity=0.7,
##        marker={
##            'size': 25,
##            'line': {'width': 0.5, 'color': 'white'}
##        },
##        name=dist
##    ))
##
##
##
##
##outbound_layout = html.Div(style={'backgroundColor': colors['background']}, children=[
##    html.H1(
##        children='dashPAD',
##        style={
##            'textAlign': 'center',
##            'backgroundColor': colors['background'],
##            'color': colors['text']
##            }
##    ),
##    
##    html.Div([
##    html.H4(children='Cumulative Outbound Usage Stats'),
##    generate_table(df_table_out),
##    ],style={'textAlign': 'left', 'padding':100}),
##    
##    html.Div([
##    dcc.Graph(
##        id='outbound_1',
##        figure={
##            'data': traces_out,
##            'layout': go.Layout(
##                title="Usage by geography",
##                xaxis={'title': 'Inbound usage'},
##                yaxis={'title': 'Outbound usage'},
##                hovermode='closest'
##            )
##        }
##    ),
##    ],style={'padding': 100}),
##
####    dcc.Graph(
####        id='inbound_2',
####        figure={
####            'data': [
####                  go.Bar(
####                      x=df_in2['month'],
####                      y=df_in2[col],
####                      name=col
####                    ) for col in cols_in
####                
####            ],
####            'layout': go.Layout(
####                barmode='group',
####                xaxis={'title': 'Month'},
####                yaxis={'title': 'Frequency'},
####                hovermode='closest'
####            )
####        }
####    ),
####
####    dcc.Graph(
####        id='inbound_3',
####        figure={
####            'data': [
####                  go.Bar(
####                      x=df_in3['district'],
####                      y=df_in3['n()'],
####                    ) 
####                
####            ],
####            'layout': go.Layout(
####                xaxis={'title': 'District'},
####                yaxis={'title': 'Frequency of incoming calls'},
####                hovermode='closest'
####            )
####        }
####    ),
##      
##    #dcc.Link('Pest', href='/pest'),
##    #html.Br(),
##    dcc.Link('Index', href='/'),
##    
##])





########            farmer profiles      ######
##
##gender = pd.read_csv(
##    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/profiles_dash/gender.csv')
##phone = pd.read_csv(
##    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/profiles_dash/phone.csv')
##irrigation = pd.read_csv(
##    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/profiles_dash/irrigation.csv')
##land = pd.read_csv(
##    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/profiles_dash/land.csv')
##sowing = pd.read_csv(
##    'X:/Dropbox (Precision Agr)/Implementation_India/Field_India/Field_Odisha/01operations/06. usage_analysis/out/profiles_dash/sowing.csv')
##
##
##profiles_layout = html.Div(style={children=[
##    html.H1(
##        children='dashPAD',
##        style={
##            'textAlign': 'center',
##            'color': colors['text']
##            }
##    ), 
##
##    html.Div([
##        html.Div([
##        dcc.Graph(
##            id='pie-1',
##            figure={
##                'data': [
##                      go.Pie(
##                          labels=['Male','Female'],
##                          values=profiles['gender'],
##                          hoverinfo='label+percent',
##                          textfont=dict(size=20),
##                          marker=dict(colors=colors),
##                          line=dict(color='#000000', width=2),
##                        ) 
##                    
##                ],
##            }
##        ),
##        ], className="four columns"),
##
##        html.Div([
##        dcc.Graph(
##            id='inbound_1',
##            figure={
##                'data': [
##                      go.Scatter(
##                          x=df_in1['month'],
##                          y=df_in1['n()'],
##                        ) 
##                    
##                ],
##                'layout': go.Layout(
##                    xaxis={'title': 'Month'},
##                    yaxis={'title': 'Frequency of incoming calls'},
##                    hovermode='closest'
##                )
##            }
##        ),
##        ], className="four columns"),
##
##        html.Div([
##        dcc.Graph(
##            id='inbound_1',
##            figure={
##                'data': [
##                      go.Scatter(
##                          x=df_in1['month'],
##                          y=df_in1['n()'],
##                        ) 
##                    
##                ],
##                'layout': go.Layout(
##                    xaxis={'title': 'Month'},
##                    yaxis={'title': 'Frequency of incoming calls'},
##                    hovermode='closest'
##                )
##            }
##        ),
##        ], className="four columns"),
##
##    ], className="row")
##
##    html.Div([
##        html.Div([
##        dcc.Graph(
##            id='inbound_1',
##            figure={
##                'data': [
##                      go.Scatter(
##                          x=df_in1['month'],
##                          y=df_in1['n()'],
##                        ) 
##                    
##                ],
##                'layout': go.Layout(
##                    xaxis={'title': 'Month'},
##                    yaxis={'title': 'Frequency of incoming calls'},
##                    hovermode='closest'
##                )
##            }
##        ),
##        ], className="four columns"),
##
##        html.Div([
##        dcc.Graph(
##            id='inbound_1',
##            figure={
##                'data': [
##                      go.Scatter(
##                          x=df_in1['month'],
##                          y=df_in1['n()'],
##                        ) 
##                    
##                ],
##                'layout': go.Layout(
##                    xaxis={'title': 'Month'},
##                    yaxis={'title': 'Frequency of incoming calls'},
##                    hovermode='closest'
##                )
##            }
##        ),
##        ], className="four columns"),
##
##        html.Div([
##        dcc.Graph(
##            id='inbound_1',
##            figure={
##                'data': [
##                      go.Scatter(
##                          x=df_in1['month'],
##                          y=df_in1['n()'],
##                        ) 
##                    
##                ],
##                'layout': go.Layout(
##                    xaxis={'title': 'Month'},
##                    yaxis={'title': 'Frequency of incoming calls'},
##                    hovermode='closest'
##                )
##            }
##        ),
##        ], className="four columns"),
##
##    ], className="row")
##        
##    dcc.Link('Pest', href='/pest'),
##    html.Br(),
##    dcc.Link('Index', href='/'),
##    
##])
##
##

#training

training_layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='dashPAD',
        style={
            'textAlign': 'center',
            'color': colors['text']
            }
    ), 

##    dcc.Graph(
##        id='inbound_1',
##        figure={
##            'data': [
##                  go.Scatter(
##                      x=df_in1['month'],
##                      y=df_in1['n()'],
##                    ) 
##                
##            ],
##            'layout': go.Layout(
##                xaxis={'title': 'Month'},
##                yaxis={'title': 'Frequency of incoming calls'},
##                hovermode='closest'
##            )
##        }
##    ),
##
        
    dcc.Link('Pest', href='/pest'),
    html.Br(),
    dcc.Link('Index', href='/'),
    
])





# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pest':
        return pest_layout
    elif pathname == '/inbound':
        return inbound_layout
    elif pathname == '/outbound':
        return outbound_layout
    elif pathname == '/training':
        return training_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here



if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
