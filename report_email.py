#!/usr/bin/env python3
import emails
import os
import datetime
import sys
import reports

def main(argv):
 path ="./descriptions/"
 fruit_list = []
 d = datetime.datetime.now()
 todays_date = d.strftime("%B %d, %Y")
 #Gets the month day year of the current date.
 for file in os.listdir(path):
        #Gets all files in path.
    with open(path+"/"+file) as file:
         new_dict = ""
         name = file.readline()
         new_dict +=  "name:" +" "+ name.strip() + "<br/>"
         #Adds Name: "name" with a new line.
         weight = file.readline()
         new_dict += "weight:" +" "+ weight.strip() + "<br/>" + "<br/>"
         #Adds weight: "weight" with two new lines.
         fruit_list.append(new_dict)
         #Adds all the new strings into a list.
         #print(fruit_list)
         #print(dict_keys)
    file.close()
 reports.generate_report("./processed.pdf", "Processed Update on" +" "+ todays_date, " ".join(fruit_list))
 #Use's report.py to make a pdf.
 sender = "automation@example.com"
 receiver = "{}@example.com" .format(os.environ.get('USER'))
 subject = "Upload Completed - Online Fruit Store"
 body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
 attachment_path = "./processed.pdf"
 message = emails.generate_email(sender, receiver, subject, body, attachment_path)
 emails.send(message)  
 #Using emails.py to send all the info to a email.  
    
if __name__ == "__main__":
    main(sys.argv)