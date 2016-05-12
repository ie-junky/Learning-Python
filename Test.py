import urllib.request
from xml.etree.ElementTree import parse
import time
import webbrowser

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
office_lat = 41.980262

data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()
print('Wrote rt22.xml')

doc = parse('rt22.xml')

for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    if lat >= office_lat:
        busid = bus.findtext('id')
        direction = bus.findtext('d')
        if direction.startswith('North'):
            print(busid, direction, lat)

busids = {'1902'}

def distance(lat1, lat2):
    'Return approx miles between lat1 and lat2'
    return 69 * abs(lat1 - lat2)


def check():
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in busids:
            lat = float(bus.findtext('lat'))
            lon = float(bus.findtext('lon'))
            dist = distance(lat, office_lat)
            direction = bus.findtext('d')
            print('%s %s %0.2f miles' % (busid, direction, dist))

            if dist < 2.7:
                # Launch a browser to see on a map
                webbrowser.open(
                    'http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false&markers=|%f,%f' % (
                    lat, lon))


# refreshrate = int(input("Enter refresh rate: "))

refreshrate = int('3')
repeat = int(3)
while True:
    while (repeat <= 3):
        check()
        time.sleep(refreshrate)
        refreshrate += 1
    #break
