from html.parser import HTMLParser
import urllib.request as urllib2
import re

def for_iamge_url():
    image = []
    class MyHTMLParser(HTMLParser):

        query = []

        result = {}

        def handle_starttag(self, tag, attrs):
            self.result['name'] = tag
            self.result['attr'] = attrs
        
        def handle_endtag(self, tag):
            pass

        def handle_data(self, data):
            tag = self.query[0]
            attr = self.query[1]

            if not len(attr):
                try:
                    if self.result['name'] == tag:
                        image.append(data)
                        #print(data)
                except:
                    pass
            else:
                pass



    parser = MyHTMLParser()
    html_page = urllib2.urlopen("https://www.vrbo.com/vacation-rentals/condos-and-apartments/usa/florida/north-west/panama-city-beach")
    parser.query = ['script', (), 'text']
    parser.feed(str(html_page.read()))

    pic = ''
    for im in image:
        x = re.search("^window.__PRELOADED_STATE__", im)
        if x:
            pic = im
            x = ''
        
    li = re.findall(r'thumbnailUrl(.*?),', pic)

    image_list = []
    for i in range(18):
        image_list.append(li[i])
    
    return image_list
