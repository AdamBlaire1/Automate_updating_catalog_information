#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module
# Post all .jpegs in a file
url = "http://localhost/upload/"
path =(r"/home/student-03-157caa2f9944/supplier-data/images/")
for file in os.listdir(path):
 #print(file)
 if file.endswith(".jpeg"):
  with open(path+"/"+file, "rb") as opened:
   r = requests.post(url, files={'file': opened})