import json

# The input parameter names for these functions are intentionally vague since they can be used for any of the json files we've created.

def open_json_as_dict(json_file):
    '''
    Opens a json file as a python dict object
    '''

    with open(json_file, "r") as file_to_read:
        return json.loads(file_to_read.read())

def cumulative_analysis(file_one, file_two):
    '''
    file_one: JSON file
    file_two: JSON file
    Aggregrates all the data between 2005-2015 for each country and sorts them by M.
    '''

    first = open_json_as_dict(file_one)
    second = open_json_as_dict(file_two)

    first_sum = {c:0.0 for c in first}
    second_sum = {c:0.0 for c in second}

    for country in first:
        for year in xrange(2005, 2016):
            try:
                first_sum[country] += first[country][str(year)]
            except KeyError:
                pass
            except Exception, e:
                print e

            try:
                second_sum[country] += second[country][str(year)]
            except KeyError:
                pass
            except Exception, e:
                print e

    first_total_sum = sum(first_sum.values())
    second_total_sum = sum(second_sum.values())

    first_to_second_ratio = {}

    for country in first:
#        if second_sum[country] < second_total_sum/10000:
	    # If a country contributes less than .01% of the world's total research, we will exclude it from our analysis. 
	    # Including such countries will lead to misleadingly high M scores. 
#            continue
        try:
            first_proportion = first_sum[country]/first_total_sum
            second_proportion = second_sum[country]/second_total_sum
            first_to_second_ratio[country] = first_proportion/second_proportion 
        except KeyError:
            pass
        except ZeroDivisionError:
            pass
        except Exception, e:
            print e

    first_to_second_tuples = []

    for country in first_to_second_ratio:
        try:
            first_to_second_tuples.append((first_to_second_ratio[country], country))
        except KeyError:
            pass
        except Exception, e:
            print e

    count = 1
    for tup in sorted(first_to_second_tuples)[::-1]:
#        print "|", count, "|", tup[1], "|", str(tup[0])[:6], "|"
#        print str(count)+".", tup[1], ":", str(tup[0])[:6]
        count += 1

def analyze_by_year(file_one, file_two):
    '''
    file_one: JSON file
    file_two: JSON file
    Analyzes scores for each year and sorts all countries based on M for that year
    '''

    first = open_json_as_dict(file_one)
    second = open_json_as_dict(file_two)

    for year in xrange(2005, 2016):
        print "YEAR:", year

        # Assess total dengue fever weight
        first_total_year_weight = 0.0
        for country in first:
            try:
                first_total_year_weight += first[country][str(year)]
            except KeyError:
                pass
            except Exception, e:
                print e

        # Assess total second weight
        second_total_year_weight = 0.0
        for country in second:
            try:
                second_total_year_weight += second[country][str(year)]
            except KeyError:
                pass
            except Exception, e:
                print e
        # Make list of tuples of (dengue fever proportion/second proportion)

        first_to_second_tuples = []

        for country in second:
            try:
                first_proportion = first[country][str(year)]/first_total_year_weight
                second_proportion = second[country][str(year)]/second_total_year_weight
                first_to_second_tuples.append((first_proportion/second_proportion, country))
            except KeyError:
                pass
            except ZeroDivisionError:
                pass
            except Exception, e:
                print e

        # Sort countries by M
        for tup in sorted(first_to_second_tuples)[::-1][:20]:
            print tup[1], ":", tup[0]

def analyze_specific_countries_by_year(file_one, file_two, countries):
    '''
    file_one: JSON file
    file_two: JSON file
    countries: List of country names
    Aggregrates all the data between 2005-2015 for each country in "countries" and sorts them by M.
    '''

    # These print statements will print a GitHub Markdown Table to display Data
    print "|" + " | ".join(countries) + "|"

    first = open_json_as_dict(file_one)
    second = open_json_as_dict(file_two)

    for year in xrange(2005, 2016):
        # Assess total dengue fever weight
        first_total_year_weight = 0.0
        for country in first:
            try:
                first_total_year_weight += first[country][str(year)]
            except KeyError:
                pass
            except Exception, e:
                print e

        # Assess total second weight
        second_total_year_weight = 0.0
        for country in second:
            try:
                second_total_year_weight += second[country][str(year)]
            except KeyError:
                pass
            except Exception, e:
                print e

        statement = "|" + str(year)
        for specific_country in countries:
            first_proportion = first[specific_country][str(year)]/first_total_year_weight
            second_proportion = second[specific_country][str(year)]/second_total_year_weight
            country_M = first_proportion/second_proportion 
            if specific_country == countries[-1]:
                statement += "|" + str(country_M) + "|"
            else:
                statement += "|" + str(country_M)

        print statement

def main():
    countries_to_analyze = ["India", "Brazil", "Germany", "Japan"]

#    analyze_specific_countries_by_year("JSON_files/dengue_fever_2005_2015.json", "JSON_files/sci_mago.json", countries_to_analyze)
#    analyze_specific_countries_by_year("JSON_files/dengue_fever_2005_2015.json", "JSON_files/rat_2005_2015.json", countries_to_analyze)
#    analyze_specific_countries_by_year("JSON_files/bias_corrected_dengue_fever_2005_2015.json", "JSON_files/sci_mago.json", countries_to_analyze)

#    analyze_by_year("JSON_files/dengue_fever_2005_2015.json", "JSON_files/sci_mago.json")
#    analyze_by_year("JSON_files/dengue_fever_2005_2015.json", "JSON_files/rat_2005_2015.json")
#    analyze_by_year("JSON_files/bias_corrected_dengue_fever_2005_2015.json", "JSON_files/sci_mago.json")

#    cumulative_analysis("JSON_files/dengue_fever_2005_2015.json", "JSON_files/sci_mago.json")
#    cumulative_analysis("JSON_files/dengue_fever_2005_2015.json", "JSON_files/rat_2005_2015.json")
#    cumulative_analysis("JSON_files/bias_corrected_dengue_fever_2005_2015.json", "JSON_files/sci_mago.json")

main()
