import json
import dash 
from dash import dcc
from dash.dependencies import Input, Output
from dash import html
import plotly.express as px
import pandas as pd

app=dash.Dash(__name__)

def get_medians(zipcode, zipcode_df):  # function to calculate median from dataframe
    try:
        median = int(zipcode_df[zipcode]['Number of Returns'].iloc[0]/2)
        for i in range(1, 7):
            if zipcode_df[zipcode]['Number of Returns'].iloc[i] < median:
                median -= zipcode_df[zipcode]['Number of Returns'].iloc[i]
            else:
                return zipcode_df[zipcode]['AGI'].iloc[i]
    except:
        return "No Information"



# neighborhood name to zipcode data
neighborhood_raw = pd.read_excel("data/neighborhoods.xlsx")

zip_codes_neighborhoods = {}
for idx, zipcodes in enumerate(neighborhood_raw["Zip Codes"]):
    if type(zipcodes) == str:
        for zipcode in zipcodes.split(","):
            zip_codes_neighborhoods[zipcode.strip(
            )] = neighborhood_raw["Neighborhood"][idx]
    else:
        zip_codes_neighborhoods[str(
            zipcodes)] = neighborhood_raw["Neighborhood"][idx]


# IRS Data


def get_income_data(year):  # function to get income data from csv
    year = str(year)
    df = pd.read_csv(f"data/income_data/formatted_data/{year}_irs_data")
    return df


zip_dfs = {}
all_income_data = {}

for i in range(2011, 2019):
    all_income_data[str(i)] = get_income_data(i)
    zip_dfs[str(i)] = {}

# Map Data

with open("C:\Users\kofij\OneDrive\Desktop\nyc-income-main\data\nyc_zip_codes.json") as json_file:
    data = json.load(json_file)
    for i in range(len(data['features'])):
        zipcode = data['features'][i]['properties']['postalCode']
        for year, df in all_income_data.items():
            if int(zipcode) in df['Zip Code'].values:
                zip_dfs[year][zipcode] = df.loc[df['Zip Code'].values ==
                                                int(zipcode)]
            try:
                data['features'][i]['properties']['neighborhood'] = zip_codes_neighborhoods[zipcode]
            except:
                data['features'][i]['properties']['neighborhood'] = "None"

            data['features'][i]['properties'][f'{year}_median_income'] = get_medians(
                zipcode, zip_dfs[year]).strip()

        data['features'][i]['properties']['current_median_income'] = data['features'][i]['properties']['2011_median_income']


# Slider



# Legend

#my dash
app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    #Map
    fig = px.choropleth_mapbox(df, geojson=data, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()
    
    #scatterplot
    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig





if __name__ == '__main__':
    app.run_server(debug=True)