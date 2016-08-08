import json
import csv
import pandas as pd
import plotly.plotly as py

def open_json_as_dict(json_file):
    '''
    Opens a json file as a python dict object
    '''

    with open(json_file, "r") as file_to_read:
        return json.loads(file_to_read.read())

def write_to_file(output_file, country_dict):
    '''
    output_file = name of save to save to
    country_dict = dict object to be converted and saved to json
    '''

    try:
        with open(output_file, "w") as f:
            f.write(json.dumps(country_dict))
        print output_file + "has been created"
    except Exception as e:
        print e
        print "Could not create" + output_file

def main():
    '''
    This the plot.ly sample choropleth method modified to use our Pubmed Data
    Sample: https://plot.ly/python/choropleth-maps/#world-choropleth-map
    '''

    df = pd.read_csv('revised_country_M_code.csv')

    data = [ dict(
            type = 'choropleth', 
            locations = df['Code'], 
            z = df['M'], 
            text = df['Country'], 
            autocolorscale = True, 
            reversescale = False, 
            marker = dict(
                line = dict (
                    color = 'rgb(180, 180, 180)', 
                    width = 0.5
                ) ), 
            colorbar = dict(
                autotick = False, 
                tickprefix = '', 
                title = 'M'), 
          ) ]

    layout = dict(
        title = 'Countries ranked by M', 
        geo = dict(
            showframe = False, 
            showcoastlines = False, 
            projection = dict(
                type = 'Mercator'
            )
        )
    )

    fig = dict( data=data, layout=layout )
    py.iplot( fig, validate=False, filename='M-world-map' )

def map_country_to_code():
    '''
    Takes our sci_mago countries and maps them to Plot.ly world map country codes
    '''

    sci_mago_dict = open_json_as_dict('../Analysis/JSON_files/sci_mago.json')

    country_to_country_code_dict = {country:None for country in sci_mago_dict}

    df = pd.read_csv('sample_plotly_gdp_data.csv')
    country = df['COUNTRY']
    code = df['CODE']

    country_code_tuples = zip(country, code)

    no_code_countries = []

    for tup in country_code_tuples:
        if tup[0] in country_to_country_code_dict:
            country_to_country_code_dict[tup[0]] = tup[1]
        else:
            no_code_countries.append(tup)

    no_code_countries = sorted(no_code_countries)

#    Some countries could not be linked to country codes due to name differences
#    For those countries, we have to associate them manually

    write_to_file("country_to_country_code.json", country_to_country_code_dict)

#map_country_to_code()

def create_csv():
    '''
    Creates a csv in the style of the Plot.ly sample csv
    '''
    
    country_to_country_code_dict = open_json_as_dict("country_to_country_code.json")
    M_results_from_2a = open("approach_2a.txt", "r").read().splitlines()

    with open("country_M_code.csv", "w") as f:
        for line in M_results_from_2a:
            country, M = line.split(", ")
            country_code = country_to_country_code_dict[country]
            f.write(country + ", " + M + ", " + country_code + '\n')

def create_revised_csv():
    '''
    Creates a modified CSV to show only countries with M values > 2.
    '''

    country_to_country_code_dict = open_json_as_dict("country_to_country_code.json")
    country_to_plot_data_dict = {}

    M_results_from_2a = open("approach_2a_simplified.txt", "r").read().splitlines()

    for line in M_results_from_2a:
        country, M = line.split(", ")
        if float(M) > 2.0:
            M = 1
        else:
            M = 0
        country_code = country_to_country_code_dict[country]
        country_to_plot_data_dict[country] = {'code':country_code, 'M':M}

    for country in country_to_country_code_dict:
        if country not in country_to_plot_data_dict and country_to_country_code_dict[country] is not None:
            country_to_plot_data_dict[country] = {'code':country_to_country_code_dict[country], 'M':0}

    with open("revised_country_M_code.csv", "w") as f:
        f.write("Country, M, Code" + '\n')
        for country in country_to_plot_data_dict:
            f.write(country + ", " + str(country_to_plot_data_dict[country]['M']) + ", " + country_to_plot_data_dict[country]['code'] + '\n')

create_revised_csv()
main()
