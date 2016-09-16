import json
import xml
import xml.etree.cElementTree as cElementTree

def process_xml(file_name, country_dict):
    '''
    file_name = Name of XML file to process
    country_dict = object to write data to
    '''
    for event, elem in cElementTree.iterparse(file_name):
        if elem.tag == "PubmedArticle":
            process_element(elem, country_dict)
            elem.clear()  # It's crucial to clear the elem in order to free up memory

def process_element(elem, country_year_count_dict):
    '''
    elem: cElementTree.elem object
    country_year_count_dict: dict object to write elem data to
    '''
    try:
        article_year = elem.find("MedlineCitation").find("DateCreated").find("Year").text
        authors = elem.find("MedlineCitation").find("Article").find("AuthorList").findall("Author")
    except:
        return  # Keys don't exist - nothing to process

    current_article_countries = []

    for author in authors:
        try:
            affiliation_info = author.find("AffiliationInfo")
            affiliation = affiliation_info.find("Affiliation").text
        except:
            continue  # Affiliation or affiliation information doesn't exist - move onto next author

        # Example Affiliation: "Department of Human Genetics and Genomic Medicine, Faculty of Medicine, University of Southampton, Southampton, UK."

        current_country_full = affiliation.split(", ")[-1]
        # "UK."

        current_country = current_country_full.split(".")[0][1:]
        # "UK"

        if current_country not in country_year_count_dict:
            if any(word in current_country_full for word in ["U.K.", "United Kingdom", "Scotland", "England", "UK"]):
                current_country = "United Kingdom"
            elif any(word in current_country_full for word in ["United States", "U.S.A", "America", "USA"]):
                current_country = "United States"
            elif any(word in current_country_full for word in ["China", "P.R.C"]):
                current_country = "China"
            elif any(word in current_country_full for word in ["Republic of Korea", "S.K", "S. Korea", "Korea, S"]):
                current_country = "South Korea"
            elif any(word in current_country_full for word in ["Netherlands"]):
                current_country = "Netherlands"
            elif any(word in current_country_full for word in ["Switzerland"]):
                current_country = "Switzerland"
            elif any(word in current_country_full for word in ["Federal Republic of Germany"]):
                current_country = "Germany"
            elif any(word in current_country_full for word in ["Brasil"]):
                current_country = "Brazil"
            else:
                continue

        current_article_countries.append(current_country)

    number_of_authors = float(len(current_article_countries))

    if number_of_authors == 0.0:
        return  # No authors found - nothing to compute.
    else:
        for country in current_article_countries:
            try:
                country_year_count_dict[country][article_year] += 1/number_of_authors
            except KeyError:
                continue
            except Exception, e:
                print e

def write_to_file(output_file, country_dict):
    '''
    output_file = name of save to save to
    country_dict = dict object to be converted and saved to json
    '''

    try:
        with open(output_file, "w") as f:
            f.write(json.dumps(country_dict))
        print output_file + " has been created"
    except:
        print "Could not create " + output_file

def main(file_location, output_file):

    with open("../Analysis/JSON_files/sci_mago.json", "r") as sci_mago:
        sci_mago_dict = json.loads(sci_mago.read())

    country_year_count_dict = {}

    for country in sci_mago_dict:
        country_year_count_dict[country] = {str(year): 0.0 for year in range(2000, 2016)}

    process_xml(file_location, country_year_count_dict)

    write_to_file(output_file, country_year_count_dict)

#main("Pubmed_XML_files/dengue_fever_2005_2015_result.xml", "../Analysis/JSON_files/dengue_fever_2005_2015.json")
#main("Pubmed_XML_files/rat_2005_2015_result.xml", "../Analysis/JSON_files/rat_2005_2015.json")
