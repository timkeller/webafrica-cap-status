# Put your username, password and account_id in settings.py
import settings

import re
import datetime 
import requests
from bs4 import BeautifulSoup
from calendar import monthrange

# Login and Fetch page
s = requests.Session()
r = s.post("https://www.webafrica.co.za/dologin.php", data={"username":settings.username, "password":settings.password})
response = s.get("https://www.webafrica.co.za/clientarea.php?action=productdetails&id="+settings.account_id+"&modop=custom&a=LoginToDSLConsole")

# Parse the page with beautiful soup
page = BeautifulSoup(response.text).find('span', {'id': 'ctl00_ctl00_contentDefault_contentControlPanel_lblAnytimeCap'})
used, total = re.findall(r"^\((.*) GB of (.*) GB\)", page.text, re.I)[0]
percentage_data = float(used)/float(total)*100

# Calculate progression through the month
start_point_in_month = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, 1)
current_point_in_month = datetime.datetime.now()
month_progression = current_point_in_month - start_point_in_month

days_in_month = float(monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1])
percentage_month = month_progression.total_seconds()/(days_in_month*24*60*60)*100

# Output
print str(round(percentage_data,1)) + "% of data used (" + used + " GB)"
print str(round(percentage_month,1)) + "% of month through"