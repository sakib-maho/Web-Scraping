# Copyright (c) 2025 sakib-maho
# Licensed under the MIT License
# See LICENSE file for details

from html.parser import HTMLParser
import urllib.request

hotel_info = []
temp = []

url = 'https://www.vrbo.com/vacation-rentals/condos-and-apartments/usa/florida/north-west/panama-city-beach'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozila'})


with urllib.request.urlopen(req) as html:
  page = html.read()


class MyHTMLParser(HTMLParser):
    hotel_info = []
    query = []
    result = {}
    def __init__(self, wanted_tag, wanted_attrs):
      super().__init__()
      self.wanted_tag = wanted_tag
      self.wanted_attrs = wanted_attrs
      self.flag = False
      self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == self.wanted_tag and all(attr in attrs for attr in self.wanted_attrs.items()):
          self.flag = True
         
       
    def handle_data(self, data):
          if self.flag == True:
            hotel_info.append(data)
            self.data.append(data)
    def handle_endtag(self, tag):
      if tag == self.wanted_tag:
        self.flag = False  
       



def hotel_names():
    parser = MyHTMLParser('div', {'class': 'CommonRatioCard__description'})
    parser.feed(str(page))
    return hotel_info


def hotel_room_info():
    parserr = MyHTMLParser('div', {'class': 'CommonRatioCard__subcaption'})
    parserr.feed(str(page))
    return hotel_info



def hotel_room_price():
    parserrr = MyHTMLParser('span', {'class': 'CommonRatioCard__price'})
    parserrr.feed(str(page))
    return hotel_info


