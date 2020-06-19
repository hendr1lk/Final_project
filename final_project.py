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

if total_results != 1:   
    print("Error, more than one species was found with that name, or that species does not exist. Need to refine species name and try again.")

# if search worked and only one species was found, isolate taxon's id from json file
taxon_id = str((json_data['results'][0]['record']['id']))

# use isolated taxon id to search api again, this time searching observations
base_occurences_url = 'https://api.inaturalist.org/v1/observations?place_id=any&taxon_id='
total_occurences_url = base_occurences_url + taxon_id

# create json file from iNaturalist api search
json_occurences = requests.get(total_occurences_url).json()

# write json file
with open('occurences.json', 'w') as json_file:
    json.dump(json_occurences, json_file)

