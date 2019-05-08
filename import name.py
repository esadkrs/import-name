import time
import re
from six.moves import urllib
import json

schoolname=str(raw_input("Enter school name: ")).replace(" ","%20")#"Florida%20Atlantic"
api_key = "df9lg2CxhAZSDcRG4LXOLdE05BBoqsxKyBVv9dLa"
url = "https://api.data.gov/ed/collegescorecard/v1/schools?fields=school.name&api_key={}&per_page=1&school.name={}".format(api_key,schoolname)

try:
	result = urllib.request.urlopen(url)
	data =json.loads(result.read())
	sname=(data['results'][0]['school.name'])
except:
	sname="School name is not found."

print sname
