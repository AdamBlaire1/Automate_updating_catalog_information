#!/usr/bin/env python3
import os
import requests
import json
path ="/home/student-00-6bb8076f1929/supplier-data/descriptions/"
url = "http://34.72.26.192/fruits/"
for file in os.listdir(path):
    #print(file)
    if file.endswith(".txt"):
        filename = file
        #Gives me the file name.
        with open(path+"/"+file) as file:
            dict_keys = ["name", "weight", "description", "image_name"]
            new_data = {}
            name = file.readline()
            new_data[dict_keys[0]] = name.strip()
            #Adds all the names into a new dictionary
            #print(dict_keys)
            weight = file.readline()
            new_data[dict_keys[1]] = int(weight.split(" ")[0])
            #Adds all the weights into a dictionary and turns it into a number and get rid of lbs.
            #print(weight)
            description = file.read()
            new_data[dict_keys[2]] = description
            #Adds all descriptions into a dictionary.
            #print(description)
            new_data[dict_keys[3]] = filename.split(".txt")[0]+'.jpeg'
            #Adds Image_name to all data and removes .txt and adds .jpeg to the filename and adds it to Image_name.
            #print(new_data)
            r = requests.post(url, data=new_data)
            #Post the new data to the url.
            r.status_code
            #Gives me feedback code telling if the data was received or not, should say 200 not 500.
        file.close()


