
#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module


url = "/mnt/c/Users/adamb/Desktop/Automate_updating_catalog_information/images"
with open('/mnt/c/Users/adamb/Desktop/Automate_updating_catalog_information/images/001.tiff', 'rb') as opened:
    r = requests.post(url, files={'file': opened})


