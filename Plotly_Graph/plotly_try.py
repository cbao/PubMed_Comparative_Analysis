import plotly.plotly as py
import pandas as pd
import json

def main():
    df = pd.read_csv('country_M_code.csv')

    data = [ dict(
            type = 'choropleth',
            locations = df['Code'],
            z = df['M'],
            text = df['Country'],
            colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
                [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
            autocolorscale = False,
            reversescale = True,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
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

def map_country_to_code():
    import csv
    sci_mago_dict = open_json_as_dict('../Analysis/JSON_files/sci_mago.json')

    country_to_country_code_dict = {country:None for country in sci_mago_dict}

    df = pd.read_csv('sample_plotly_gdp_data.csv')
    country = df['COUNTRY']
    code = df['CODE']
    
    country_code_tuples = zip(country,code)

    no_code_countries = []

    for tup in country_code_tuples:
        if tup[0] in country_to_country_code_dict:
            country_to_country_code_dict[tup[0]] = tup[1]
        else:
            no_code_countries.append(tup)

    no_code_countries = sorted(no_code_countries)
    no_code_sci_mago_countries = sorted([country for country in country_to_country_code_dict if country_to_country_code_dict[country] is None])

#    print no_code_countries
#    print no_code_sci_mago_countries

    write_to_file("country_to_country_code.json",country_to_country_code_dict)

#map_country_to_code()

def create_csv():
    country_to_country_code_dict = open_json_as_dict("country_to_country_code.json")
    M_results_from_2a = open("approach_2a.txt","r").read().splitlines()

#    for line in M_results_from_2a:
#        line = line.split(",")
#        print len(line)

    with open("country_M_code.csv","w") as f:
        for line in M_results_from_2a:
            country, M = line.split(",")
            country_code = country_to_country_code_dict[country]
            f.write(country + "," + M + "," + country_code + '\n')

main()
