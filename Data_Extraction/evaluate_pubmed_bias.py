import json

def open_json_as_dict(json_file):
    with open(json_file, "r") as f:
        return json.loads(f.read())

def evaluate_bias_by_year():
    # Evaluates the bias in PubMed Rat data by country by year

    rat = open_json_as_dict("../Analysis/JSON_files/rat_2005_2015.json")
    sci_mago = open_json_as_dict("../Analysis/JSON_files/sci_mago.json")

    pubmed_rat_to_sci_mago_bias = {country:{} for country in sci_mago}

    for year in xrange(2005, 2016):
        # Evaluate rat data
        total_rat_data_weight_for_year = 0.0

        for country in rat:
            try:
                total_rat_data_weight_for_year += rat[country][str(year)]
            except:
                pass

        # Evaluate SciMago data
        total_sci_mago_weight_for_year = 0.0

        for country in sci_mago:
            try:
                total_sci_mago_weight_for_year += sci_mago[country][str(year)]
            except:
                pass

        for country in sci_mago:
            try:
                pubmed_rat_to_sci_mago_ratio = (rat[country][str(year)]/total_rat_data_weight_for_year)/(sci_mago[country][str(year)]/total_sci_mago_weight_for_year)
                pubmed_rat_to_sci_mago_bias[country][str(year)] = pubmed_rat_to_sci_mago_ratio
            except Exception as e:
                pass

    output_file = "../Analysis/JSON_files/pubmed_rat_to_sci_mago_bias.json"

    try:
        with open(output_file, "w") as bias:
            bias.write(json.dumps(pubmed_rat_to_sci_mago_bias))
        print "../Analysis/JSON_files/pubmed_rat_to_sci_mago_bias.json has been created"
    except:
        print "Could not create ../Analysis/JSON_files/pubmed_rat_to_sci_mago_bias.json"

def evaluate_cumulative_bias():
    # Evaluates the bias in the aggregated 2005-2015 PubMed Rat data

    rat = open_json_as_dict("../Analysis/JSON_files/rat_2005_2015.json")
    sci_mago = open_json_as_dict("../Analysis/JSON_files/sci_mago.json")

    pubmed_rat_to_sci_mago_bias = {}

    rat_sum = {country:0.0 for country in rat}

    sci_mago_sum = {country:0.0 for country in sci_mago}

    for country in rat:
        for year in xrange(2005, 2016):
            try:
                rat_sum[country] += rat[country][str(year)]
            except:
                pass
            try:
                sci_mago_sum[country] += sci_mago[country][str(year)]
            except:
                pass

    rat_total_sum = sum(rat_sum.values())
    sci_mago_total_sum = sum(sci_mago_sum.values())

    for country in rat:
        try:
            pubmed_rat_to_sci_mago_bias[country] = (rat_sum[country]/rat_total_sum)/(sci_mago_sum[country]/sci_mago_total_sum)
        except Exception as e:
            pass

# Uncomment the lines below to print countries sorted by bias factor
#    rat_to_sci_mago_tuples = []

#    for country in pubmed_rat_to_sci_mago_bias:
#       try:
#           rat_to_sci_mago_tuples.append((pubmed_rat_to_sci_mago_bias[country], country))
#       except Exception as e:
#           print e

#    for tup in sorted(rat_to_sci_mago_tuples)[::-1][:50]:
#       print tup[1], ":", tup[0]

    try:
        with open("../Analysis/JSON_files/pubmed_rat_to_sci_mago_bias_cumulative.json", "w") as bias:
            bias.write(json.dumps(pubmed_rat_to_sci_mago_bias))
            print "../Analysis/JSON_files/pubmed_rat_to_sci_mago_bias_cumulative.json has been created"
    except:
        print "Could not create ../Analysis/JSON_files/pubmed_rat_to_sci_mago_bias_cumulative.json"

def unbias_dengue_data():
    # Corrects the assigned scores in dengue_fever_2005_2015.json by dividing each score by its bias factor

    dengue_file = "../Analysis/JSON_files/dengue_fever_2005_2015.json"
    bias_file = "../Analysis/JSON_files/pubmed_rat_to_sci_mago_bias.json"

    with open(dengue_file, "r") as dengue:
        dengue_dict = json.loads(dengue.read())

    with open(bias_file, "r") as bias:
        bias_dict = json.loads(bias.read())

    bias_corrected_dengue_dict = {c:{} for c in dengue_dict}

    for country in dengue_dict:
        for year in xrange(2005, 2016):
            try:
                bias_corrected_dengue_dict[country][str(year)] = dengue_dict[country][str(year)]/bias_dict[country][str(year)]
            except Exception as e:
                pass

    try:
        with open("../Analysis/JSON_files/bias_corrected_dengue_fever_2005_2015.json", "w") as unbias:
            unbias.write(json.dumps(bias_corrected_dengue_dict))
        print "../Analysis/JSON_files/bias_corrected_dengue_fever_2005_2015.json has been created"
    except:
        print "Could not create ../Analysis/JSON_files/bias_corrected_dengue_fever_2005_2015.json"


def main():
    evaluate_bias_by_year()

    evaluate_cumulative_bias()

    unbias_dengue_data()

#main()
