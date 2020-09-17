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
        with open(path+"/"+file) as file:
            dict_keys = ["name", "weight", "description", "image_name"]
            new_data = {}
            name = file.readline()
            new_data[dict_keys[0]] = name.strip()
            #print(dict_keys)
            weight = file.readline()
            new_data[dict_keys[1]] = int(weight.split(" ")[0])
            #print(weight)
            description = file.read()
            new_data[dict_keys[2]] = description
            #print(description)
            new_data[dict_keys[3]] = filename.split(".txt")[0]+'.jpeg'
            #print(new_data)
            r = requests.post(url, data=new_data)
            r.status_code
        file.close()

#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["Normal"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])




