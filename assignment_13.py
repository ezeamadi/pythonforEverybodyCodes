import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

#    new_list = []
    comments = tree.findall('.//count')
###
#    uh = urllib.urlopen(url)
#    data = uh.read()
    print(comments)
#    tree = ET.fromstring(data)
#    comments = tree.find('comments').findall('comment')
    #total_count = 0
    #for comment in comments:
    #    count = comment.find('count').text
    #    count = int(count)
    #    total_count += count
    #print(total_count)

    #print('Count:', tree.findall('count').text)

    #results = tree.findall('result')
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    #print('lat', lat, 'lng', lng)
    #print(location)
