#!/usr/bin/env python3
import cgi
import os

form = cgi.FieldStorage()

class resClass:
  def __init__(self, name, suburb):
    self.name = name
    self.suburb = suburb
  #End Class

resList = []

def txtToClass():
  path = "cgi-bin/restaurants.txt"
  resDoc = open(path, "r").readlines()
  
  for line in resDoc:
      row = line.split(',')
      name, suburb = [i.strip() for i in row]
      res = resClass(name, suburb)
      resList.append(res) 

  #resDoc.close()

txtToClass()

resName = form.getvalue("restaurant")
resSuburb = form.getvalue("suburb")

resList.append(resClass(resName, resSuburb))

divSingle = """
<div class="resDiv">
  <p class="resName">{}</p>
  <p class="resSuburb">{}</p>
</div>
<hr>
"""

divAll = ""

i = 0
while i < len(resList):
  divAll = divAll + divSingle.format(resList[i].name, resList[i].suburb)
  i = i+1

print("""
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8" />
        <title>Restaurants in Berlin</title>
        <link rel="stylesheet" href="/style.css">
      </head>
      <body>
        <div class="main">
          <h1>Restaurants in Berlin</h1>
          {}
          <a href="/index.html" id="back">Go Back</a>
        </div>
      </body>
    </html>
""".format(divAll))
