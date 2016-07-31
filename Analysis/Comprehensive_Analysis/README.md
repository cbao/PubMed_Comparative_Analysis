# Comparative Analysis
## Addressing potential PubMed bias  
* Since we will be working with PubMed data, it is important to assess whether there exists any bias in the articles available through PubMed.  To do this, we will search for a topic that should be of equal interest to all countries. 

  * We must first rule out diseases of an infectious nature, specifically those caused by bacteria and viruses, as they tend to spread in developing countries more frequently.  
  * Toxicological studies must also be ruled out as there is great variation from country to country.  
  * Genetic Diseases must also be ruled out as some populations are more likely to succumb to certain genetic diseases than others.  

After careful consideration, I simply settled on the term "Rat." Rats are one of the most commonly animals used in research and their use is limited by neither geography nor cost (unlike, for example, chimpanzees). Furthermore, researchers from all fields of medicine perform experiments on rats, so it should serve as a fairy good yardstick in gauging how much research a country produces.

To account for this potential bias, we will perform analysis under two separate assumptions:  

* 1) PubMed has little to no bias. So we will simply compare statistics from PubMed on Dengue Fever to the Medicine report from SciMago.  

* 2) PubMed does have some inherent bias:  

  * 2a) We will compare PubMed Dengue Fever data to PubMed Rat Data. If some bias does exist, there is no reason to think that one subset of data is any more or less biased than the another. Thus comparing two samples from the same biased data will still allow us to gauge the relative investment of countries between the two samples.  

  * 2b) We will measure of the bias of the PubMed Data by weighing the PubMed Rat Data against the SciMago data. We will then assess the bias factor per country per year, and divide the Dengue Fever data by the bias factor. We then perform analysis of the "bias corrected" Dengue Fever data against the SciMago Data.  


# Approach 1


**Pubmed Dengue Fever data to SciMago Medicine data Analysis**    

|Year|	  India	   | Brazil      |Germany	      |Japan	       |
|:--:|:-----------:|:-----------:|:------------:|:------------:|
|2005|5.42564979124|7.18501464972|0.244522538614|0.330236822975|
|2006|5.77626592869|4.84405827691|0.272399816314|0.520587650437|
|2007|2.95890644095|5.88589312489|0.233934610135|0.373594201448|
|2008|4.65363429819|5.79791817298|0.208234840533|0.733641053162|
|2009|3.16743157815|6.66352475062|0.285129312662|0.478617610662|
|2010|3.43790242913|4.33660439074|0.160623454787|0.499795986476|
|2011|3.33958381939|4.55496907764|0.283700681021|0.530066087607|
|2012|4.4860236488|4.79903399377|0.250190666255|0.574517741905|
|2013|3.74258199329|4.32237888053|0.233992446192|0.521850724051|
|2014|3.70105384295|5.40843381494|0.411121278957|0.513432649057|
|2015|4.35930618431|4.92399725166|0.326207896899|0.502819328735|


**Top countries sorted by M**  

|Rank   |	  Country	      |    Multiple	    |
|:-----:|:-------------:|:-------------:|
| 1 | Sri Lanka | 30.97 |
| 2 | Cambodia | 19.88 |
| 3 | Puerto Rico | 17.75 |
| 4 | Thailand | 14.30 |
| 5 | Cuba | 14.08 |
| 6 | Vietnam | 14.00 |
| 7 | Indonesia | 13.21 |
| 8 | Gabon | 10.10 |
| 9 | Malaysia | 10.07 |
| 10 | Singapore | 10.01 |
| 11 | Colombia | 9.325 |
| 12 | Philippines | 7.285 |
| 13 | Trinidad and Tobago | 7.273 |
| 14 | Jamaica | 6.983 |
| 15 | Sudan | 5.867 |

# Approach 2a  

**Pubmed Dengue Fever to Pubmed Rat Analysis**   

|Year|	  India	   | Brazil      |Germany	      |Japan	       |
|:--:|:-----------:|:-----------:|:------------:|:------------:|
|2005|4.19879235461|3.67788012548|0.323426820697|0.172058963973|
|2006|4.09845365784|2.870575511|0.385823328794|0.249159503623|
|2007|2.28675545426|3.08097042972|0.332519633589|0.189641029006|
|2008|3.74110233886|3.03847362578|0.298973302062|0.350728344268|
|2009|2.27177451949|3.54762577931|0.377037426393|0.24586579415|
|2010|2.39562896863|2.16062859691|0.229031450681|0.282579084072|
|2011|2.23878967681|2.23999084944|0.42141024484|0.288593981776|
|2012|3.06705118962|2.35915044248|0.394994535987|0.334136251767|
|2013|2.52717556267|1.95306766158|0.364272869989|0.315957855914|
|2014|2.5793825404|2.26380511365|0.634520768679|0.332124960401|
|2015|3.14793507668|2.09246510766|0.530588237269|0.31295102915|

**Top countries sorted by M**  

|Rank   |	  Country	      |    Multiple	    |
|:-----:|:-------------:|:-------------:|
| 1 | Sri Lanka | 110.4 |
| 2 | Colombia | 57.09 |
| 3 | Indonesia | 40.06 |
| 4 | Cuba | 31.58 |
| 5 | Puerto Rico | 29.49 |
| 6 | Thailand | 21.35 |
| 7 | Singapore | 20.11 |
| 8 | Malaysia | 10.64 |
| 9 | Bangladesh | 8.800 |
| 10 | Venezuela | 8.787 |
| 11 | Pakistan | 8.452 |
| 12 | Ghana | 3.559 |
| 13 | India | 3.023 |
| 14 | Mexico | 2.580 |
| 15 | Brazil | 2.567 |


# Approach 2b  

**Bias Corrected Pubmed Dengue Fever data to SciMago Medicine data Analysis**  

|Year|	  India	   | Brazil      |Germany	      |Japan	       |
|:--:|:-----------:|:-----------:|:------------:|:------------:|
|2005|3.21716208205|2.81803325402|0.247813279626|0.131833519741|
|2006|2.82369933012|1.97773180428|0.265819542201|0.17166267627|
|2007|1.66234257987|2.23969219056|0.241723068606|0.137858360333|
|2008|2.61152968761|2.12104972279|0.208702565025|0.244830908214|
|2009|1.62629832632|2.53964370927|0.269910297102|0.176008281674|
|2010|1.53431645553|1.38380694754|0.146686623102|0.180982006962|
|2011|1.37421013065|1.37494743242|0.258669330852|0.177144274654|
|2012|1.90078975336|1.46207177855|0.244795903368|0.207079283755|
|2013|1.80250748593|1.39302513547|0.259817554734|0.225356880201|
|2014|1.24758674082|1.09494935294|0.306902789865|0.16064104118|
|2015|1.86476636437|1.23952955075|0.314308609959|0.185385193354|

**Top countries sorted by M**  

|Rank   |	  Country	      |    Multiple	    |
|:-----:|:-------------:|:-------------:|
| 1 | Vietnam | 137.2 |
| 2 | Sri Lanka | 78.45 |
| 3 | Philippines | 45.26 |
| 4 | Puerto Rico | 44.79 |
| 5 | Indonesia | 39.35 |
| 6 | Colombia | 35.47 |
| 7 | Nepal | 34.39 |
| 8 | Kenya | 25.68 |
| 9 | Cuba | 22.36 |
| 10 | Ecuador | 21.28 |
| 11 | Peru | 17.71 |
| 12 | Gabon | 14.64 |
| 13 | Thailand | 13.70 |
| 14 | Singapore | 13.53 |
| 15 | Sudan | 12.75 |

## Side by Side Comparison  
![alt text](https://upload.wikimedia.org/wikipedia/commons/4/49/Dengue06.png "Dengue Worldwide Distribution 2006")
> Red: Epidemic dengue  
> Blue: Aedes aegypti (A mosquito that can spread dengue fever, chikungunya, Zika fever and yellow fever viruses, and other diseases.)  

|Rank   |	  Country  |  M (1) |  Country  |  M (2a) |  Country  |  M (2b) |
|:-----:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| 1 | Sri Lanka | 30.97 |Sri Lanka | 110.4 |Vietnam | 137.2 |
| 2 | Cambodia | 19.88 |Colombia | 57.09 |Sri Lanka | 78.45 |
| 3 | Puerto Rico | 17.75 |Indonesia | 40.06 |Philippines | 45.26 |
| 4 | Thailand | 14.30 |Cuba | 31.58 |Puerto Rico | 44.79 |
| 5 | Cuba | 14.08 |Puerto Rico | 29.49 |Indonesia | 39.35 |
| 6 | Vietnam | 14.00 |Thailand | 21.35 |Colombia | 35.47 |
| 7 | Indonesia | 13.21 |Singapore | 20.11 |Nepal | 34.39 |
| 8 | Gabon | 10.10 |Malaysia | 10.64 |Kenya | 25.68 |
| 9 | Malaysia | 10.07 |Bangladesh | 8.800 |Cuba | 22.36 |
| 10 | Singapore | 10.01 |Venezuela | 8.787 |Ecuador | 21.28 |
| 11 | Colombia | 9.325 |Pakistan | 8.452 |Peru | 17.71 |
| 12 | Philippines | 7.285 |Ghana | 3.559 |Gabon | 14.64 |
| 13 | Trinidad and Tobago | 7.273 |India | 3.023 |Thailand | 13.70 |
| 14 | Jamaica | 6.983 |Mexico | 2.580 |Singapore | 13.53 |
| 15 | Sudan | 5.867 |Brazil | 2.567 |Sudan | 12.75 |

# Discussion
## Comments
All three methods gave expected results for comparative analysis between Brazil, India, Germany, and Japan. The top ranked countries of these approach also produced results that match our distribution map.  

The three different approaches, however, produced significantly different relative rankings of when sorted by **M**. It is possible that the search term "Rat" does not produce a distribution that is close to the total research output. This could be explained by cultural and ethical differences in using rats for medical studies.

## Looking Ahead
To gather a more reliable metric to represent total research output, I will combine "Rat" data with "Mice"/"Mouse" data to increase the sample size. This should give a yield of ~1 million PubMed articles instead of the ~400,000 from "Rat." Hopefully this will result in less disparity in the relative rankings produced by the three different approaches.
