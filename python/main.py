# Copyright (c) 2025 sakib-maho
# Licensed under the MIT License
# See LICENSE file for details

from html.parser import HTMLParser
import urllib.request as urllib2
import re
from image_url import for_iamge_url
from room_information import hotel_names, hotel_room_info, hotel_room_price
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",

)

image_urls = for_iamge_url()

names = hotel_names()

room_info = hotel_room_info()

price = hotel_room_price()


names_t = []

room_info_t = []

price_t = []

final_room = []


for i in range(len(names)):
    if i < 6:
        names_t.append(names[i])
    elif i >= 6 and i <12:
        room_info_t.append(names[i])
    else:
        price_t.append(names[i])



for info in room_info_t:
    temp = info.split('\\xc2\\xb7')
    final_room.append(temp)



def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
      
image_urls_r = []

flag = 1
temp = []
for url in image_urls:
    if flag < 4:
        temp.append(Find(url))
    flag = flag + 1
    if flag > 3:
        flag = 1
        image_urls_r.append(temp)
        temp = []
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

database = []

for x in mycursor:
  database.append(x[0])

creat = True

if 'My_hotel' in database:
    creat = False

if creat:
  database="My_hotel"
  mycursor = mydb.cursor()

  mycursor.execute("CREATE DATABASE My_hotel")
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database= database
  )

  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE Hotel_data (Title VARCHAR(255), Sleeps VARCHAR(255), Bedrooms VARCHAR(255), Bathrooms VARCHAR(255), Price VARCHAR(255), Picture_1 VARCHAR(255), Picture_2 VARCHAR(255), Picture_3 VARCHAR(255), PRIMARY KEY (Title))")
  
  
  for i in range(len(image_urls_r)):

    sql = "INSERT INTO Hotel_data(Title, Sleeps, Bedrooms, Bathrooms, Price, Picture_1, Picture_2, Picture_3) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (str(names_t[i]), str(final_room[i][0]), str(final_room[i][1]), str(final_room[i][2]), str(price_t[i]), str(image_urls_r[i][0]), str(image_urls_r[i][1]), str(image_urls_r[i][2]))
    mycursor.execute(sql, val)
    mydb.commit()

else:
  print("====================================================")
  print('Database and Table Already Exist')
  print("====================================================")
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "My_hotel"
  )
  mycursor = mydb.cursor()
  
  try:
    for i in range(len(image_urls_r)):
        sql = "INSERT INTO Hotel_data(Title, Sleeps, Bedrooms, Bathrooms, Price, Picture_1, Picture_2, Picture_3) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (str(names_t[i]), str(final_room[i][0]), str(final_room[i][1]), str(final_room[i][2]), str(price_t[i]), str(image_urls_r[i][0]), str(image_urls_r[i][1]), str(image_urls_r[i][2]))
        mycursor.execute(sql, val)
        mydb.commit()
  except:
       print("====================================================")
       print('Dublicate Entry')
       print("====================================================")
