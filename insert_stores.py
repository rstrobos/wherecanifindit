import json,  httplib
import json,httplib
import csv

f = open('companyresults.txt', 'rU')
reader = csv.reader(f,delimiter = '\n')

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()

for row in reader:
  
  # print row
  lst = row[0].split('\t')
  naics = 445120
  # print 
  # print type(row[0])
  # print lst
  # print
  
  name = lst[0]
  if name == 'Company Name':
    continue

  
  addr = lst[1]
  city = lst[2]
  state = lst[3]
  postal_code = lst[4]
  country = lst[5]
  phone_num = int(''.join(lst[6].split('-')))

  dossier_id = lst[7]
  lat = float(lst[8])
  lng = float(lst[9])
  # print addr, city, state, postal_code, country
  # print dossier_id, lat, lng
  # print
  # print
  # print phone_num
  # print
  #print lst

 
  connection.request('POST', '/1/classes/Stores', json.dumps({
  	"NAME":name,
    "NAICS":naics,
  	"ADDRESS":addr,
         "LOCATION": {
           "__type": "GeoPoint",
           "latitude": lat,
           "longitude": lng
         },
    "CITY":city,
    "STATE":state,
    "COUNTRY":country,
  	"PHONE_NUMBER":phone_num,
    "DOSSIER_ID":dossier_id,
       }), {
         "X-Parse-Application-Id": "Fw1grbivm1pprw3SfNRsniIsF5yySLLJzlADsbUN",
         "X-Parse-REST-API-Key": "pwrkNxNJeCoYgg2Ebidpfb5GKiRX5qEHlzHb5jEW",
         "Content-Type": "application/json"
       })
  result = json.loads(connection.getresponse().read())
  print result
 

f.close()
