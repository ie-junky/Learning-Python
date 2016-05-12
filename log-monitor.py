# monitor.py
#
# Periodically monitor the bus system and see whether an identified
# bus returns to within a half-mile of Dave's office

import urllib
from xml.etree.ElementTree import parse
import time
import webbrowser

# Set of error ids that you want to monitor.  Change to match
# the output of the find_north.py script
errid = { 'User Unknown' }

def check():
    u = open('errors.txt')
    doc = parse(u)
    
    for bus in doc.findall(errid):
        busid = bus.findtext('id')
        if busid in busids:
            lat = float(bus.findtext('lat'))
            lon = float(bus.findtext('lon'))
            dist = distance(lat, office_lat)
            direction = bus.findtext('d')
            print('%s %s %0.2f miles' % (busid, direction, dist))

            if dist < 0.5:
                # Launch a browser to see on a map
                webbrowser.open('http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false&markers=|%f,%f' % (lat, lon))
while True:
    check()
    time.sleep(60)

