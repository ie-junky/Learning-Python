import http
import json
import pycurl
import cStringIO
import base64

h = http.request ('https://services.cro.ie')
headers = {'User-Agent': 'Agent name here', 'Host': 'services.cro.ie',
'Content-type': 'application/json',
'Authorization': 'Basic dGVzdEBjcm8uaWU6ZGEwOTNhMDQtYzlkNy00NmQ3LTljODMtOWM5Zjg2MzBkNWUw' }
h.getresponse('GET', '/cws/companies?company_name=ryanair', headers=headers, body=None)
res = h.getresponse()

json_data = json.loads(res.read())

for item in json_data:
    assert item in json_data
    print(item['company_num'], item['company_name'],"(" + item['company_status_desc'] + " / " + item['company_status_date'] + ")")