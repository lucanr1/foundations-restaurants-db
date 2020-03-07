#!/usr/bin/env python3
import cgi
import os
import sqlite3

form = cgi.FieldStorage()

#Database Stuff

db_connection = sqlite3.connect('cgi-bin/restaurants.db')
db_cursor = db_connection.cursor()
db_cursor.execute("SELECT * from restaurants WHERE NEIGHBORHOOD_ID = 1")
list_restaurants = db_cursor.fetchall()

db_connection.close()
print(list_restaurants)

#End Database Stuff

resName = form.getvalue("restaurant")
resSuburb = form.getvalue("suburb")

divSingle = """
<div class="resDiv">
  <p class="resName">{}</p>
  <p class="resSuburb">{}</p>
</div>
<hr>
"""

divAll = ""

i = 0
while i < len(list_restaurants):
  divAll = divAll + divSingle.format(list_restaurants[i][1], "Kreuzberg")
  i = i + 1

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
