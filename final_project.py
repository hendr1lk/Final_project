#!/usr/bin/python3

# final project code
# Lillian Hendrick
# 6/19/2020

# This script uses iNaturalist's API to search for a specific species, and returns a json file with it's observations

# chunk of code - use iNat's api to get taxon id

# import modules needed for script
import urllib.parse, urllib.request, urllib.error
import requests
import json
import csv

# use iNaturalist's api and the search function to look up a taxon

main_api = 'https://api.inaturalist.org/v1/search?'
taxa = input('Enter species name (Genus and specific epithet, seperate by a space): ')
url = main_api + urllib.parse.urlencode(
    {'q': taxa})

# create json file from iNaturalist api search
json_data = requests.get(url).json()

# isolate total result amount from json file
total_results = json_data['total_results']

# test to see how many results came up

# if more than one results were found, tell user to try again
if total_results > 1:
    print(str(total_results) +" species came up. Please be more specific and try again!")

# if no results were found, print an error message    
elif total_results == 0:
    print("Sorry. That species wasn't found. Please try again (try checking your spelling).")

# if search worked and only one species was found, isolate taxon's id from json file
taxon_id = str((json_data['results'][0]['record']['id']))

# use isolated taxon id to search api again, this time searching observations
base_occurences_url = 'https://api.inaturalist.org/v1/observations?place_id=any&taxon_id='
total_occurences_url = base_occurences_url + taxon_id

# create json file from iNaturalist api search
json_occurences = requests.get(total_occurences_url).json()

# write json files
with open('observations.json', 'w') as json_file:
    json.dump(json_occurences, json_file) 
with open ('taxon_info.json', 'w') as json_file:
    json.dump(json_data, json_file) 

# Write code for converting json to csv
json_results = json_occurences['results']
occurences_file = open('occurences_file.csv', 'w') 
csv_writer = csv.writer(occurences_file) 
count = 0

for row in json_results:
    if count == 0:

    #writing headers of csv file
        header = row.keys()
        csv_writer.writerow(header)
        count += 1
        
        # writing data of CSV file
        csv_writer.writerow(row.values())

total_observations = json_occurences['total_results']

print("Yay! Your search worked. It found " + str(total_observations) + 
        " observations for " + str(taxa) + 
        ". There is now a json file with all the taxon specifc data on iNaturalist called 'taxon_info.json', and a json file with the occurence records called 'observations.json' in this folder. There is also a csv called 'occurences_file.csv' made from the json file in this folder :).")
