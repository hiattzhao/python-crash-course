import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal.maps.world import COUNTRIES
from country_codes import get_country_code
import datetime

now = datetime.datetime.now()

# Make an API call and store the response
url = 'https://api.covid19api.com/summary'
r = requests.get(url)

# Store API reponse in a variable
response_dict = r.json()
countries_list = response_dict['Countries']
global_data = response_dict['Global']

# Get country codes from COUNTRIES
country_codes = [code for code in COUNTRIES.keys()]

corona_virus = {}
for country in countries_list:
  country_code = country['CountryCode'].lower()
  # total_deaths = country['TotalDeaths']
  if country_code in country_codes:
    total_confirmed = country['TotalConfirmed']
    corona_virus[country_code] = total_confirmed

# Group the countries into 3 levels
cv1, cv2, cv3 = {}, {}, {}
for cd, cv in corona_virus.items():
  if cv < 1000:
    cv1[cd] = cv
  elif cv < 100000:
    cv2[cd] = cv
  else:
    cv3[cd] = cv

# See how many countries are in each level
# print(len(cv1), len(cv2), len(cv3))

# Make visualization
wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Coronavirus Cases Confirmed by Country\n' + 'Total Confirmed Worldwide: ' + "{:,}".format(global_data['TotalConfirmed']) + '\nTotal Deaths Worldwide: ' + "{:,}".format(global_data['TotalDeaths']) + '\nUpdated on: ' + now.strftime('%Y-%m-%d')
wm.add('0-1000 cases', cv1)
wm.add('1000-100,000 cases', cv2)
wm.add('>100,000 cases', cv3)
wm.render_to_file('corona_virus_cases.svg')
