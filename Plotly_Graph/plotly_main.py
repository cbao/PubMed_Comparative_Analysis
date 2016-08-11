import json
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

    df = pd.read_csv("country_M_code.csv")

    data = [ dict(
            type = "choropleth", 
            locations = df["Code"], 
            z = df["M>2"], 
            text = df["Country"], 
            autocolorscale = True, 
            reversescale = False, 
            marker = dict(
                line = dict (
                    color = "rgb(180, 180, 180)", 
                    width = 0.5
                ) ), 
            colorbar = dict(
                autotick = False, 
                tickprefix = "", 
                title = "M"), 
          ) ]

    layout = dict(
        title = "Countries ranked by M", 
        geo = dict(
            showframe = False, 
            showcoastlines = False, 
            projection = dict(
                type = "Mercator"
            )
        )
    )

    fig = dict( data=data, layout=layout )
    py.iplot( fig, validate=False, filename="M-world-map" )

def map_country_to_code():
    '''
    Takes our sci_mago countries and maps them to Plot.ly world map country codes
    '''

    sci_mago_dict = open_json_as_dict("../Analysis/JSON_files/sci_mago.json")

    country_to_country_code_dict = {country:None for country in sci_mago_dict}

    df = pd.read_csv("sample_plotly_gdp_data.csv")
    country = df["COUNTRY"]
    code = df["CODE"]

    country_code_tuples = zip(country, code)

    no_code_countries = []

    for tup in country_code_tuples:
        if tup[0] in country_to_country_code_dict:
            country_to_country_code_dict[tup[0]] = tup[1]
        else:
            no_code_countries.append(tup)

    no_code_countries = sorted(no_code_countries)

#    Some countries could not be linked to their country codes due to name differences
#    For those countries, we have to associate them manually

    write_to_file("country_to_country_code.json", country_to_country_code_dict)

def create_csv():
    '''
    Creates a csv in the style of the Plot.ly sample csv
    '''
    
    country_to_country_code_dict = open_json_as_dict("country_to_country_code.json")
    M_results_from_2a = open("../Analysis/Results/approach_2a.txt", "r").read().splitlines()

    with open("country_M_code.csv", "w") as f:
        f.write("Country,M,Code,M>2" + "\n")
        for line in M_results_from_2a: # Example: "1. Sri Lanka : 110.4"
            current_line = line.split(" : ") # ["1. Sri Lanka", "110.4"]
            country = current_line[0].split(". ")[1] # "Sri Lanka"
            M = current_line[1] # "110.4""
            M_greater_than_two = "1" if float(M) > 2 else "0" # "1"
            country_code = country_to_country_code_dict[country] # "LKA"
            statement = ",".join([country, M, country_code, M_greater_than_two]) + "\n" # "Sri Lanka, 110.4, LKA, 1"
            f.write(statement)

#map_country_to_code()
#create_csv()
#main()
