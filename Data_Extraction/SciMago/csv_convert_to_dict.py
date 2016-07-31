import csv
import json

def convert_to_json():

    countries_scimago_dict = {}

    for year in xrange(2005,2016):

	csv_location = "SciMago_Medicine_CSV_files/" + str(year) + ".csv"

	with open(csv_location, "r") as csvfile:
	     reader = csv.reader(csvfile, delimiter=",", quotechar="|")
	     for row in reader:
		if row[2] == "Documents": # Skip headers
		    continue

		country = row[1]

		try:
		    countries_scimago_dict[country][str(year)] = int(row[2])
		except:
		    countries_scimago_dict[country] = {}
		    countries_scimago_dict[country][str(year)] = int(row[2])

    try:
	with open("../../Analysis/JSON_files/sci_mago.json","w") as f:
	    f.write(json.dumps(countries_scimago_dict))
	print "../../Analysis/JSON_files/sci_mago.json has been created"
    except:
	print "Could not create ../../Analysis/JSON_files/sci_mago.json"	

def main():
    convert_to_json()

