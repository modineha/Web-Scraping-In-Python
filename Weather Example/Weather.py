'''
Author - Neha Modi
Website scrapped - http://forecast.weather.gov
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

webpage = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168") # Downloading web page from web server
soup = BeautifulSoup(webpage.content,'html.parser') # BeautifulSoup object 'soup' is created
seven_day_data = soup.find(id = "seven-day-forecast") # seven_day_data object contains the actual data we want to access

periods = [pt.get_text() for pt in seven_day_data.select(" .tombstone-container .period-name")]
short_desc = [sd.get_text() for sd in seven_day_data.select(".tombstone-container .short-desc")]
temp = [t.get_text() for t in seven_day_data.select(".tombstone-container .temp")]
img_desc = [d["title"] for d in seven_day_data.select(".tombstone-container img")]

#print(periods)
#print(short_desc)
#print(temp)
#print(img_desc)

# Creating table using pandas dataframe.
weather = pd.DataFrame({
		"PERIOD" : periods,
		"SHORT_DESC" : short_desc,
		"TEMP" : temp,
		"IMAGE_DESC" : img_desc
		})
print weather

# Here we are extracting numerical values from TEMP column.
temp_nums = weather["TEMP"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print " Temperature value as numrical value : "+temp_nums

# Calculating mean
print ' Mean value : '
print weather["temp_num"].mean()

# Selecting rows that happen at night only
is_night = weather["TEMP"].str.contains("Low")
weather["is_night"] = is_night
is_night

print weather["is_night"]
