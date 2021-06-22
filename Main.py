#  Created By ANJANA  T A .
#Import statement 
import requests
from datetime import datetime

#Setting up API Key and Fetching Data.
apikey='583ff7e9cd28634a77a07de1b53294f9'
location=input("Enter the Town :")
print("")
print ("Loading.................")
print("")
api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+apikey
api_linkfinal = requests.get(api_link)
api_data = api_linkfinal.json()


#Temperature and Weather
temperature = ((api_data['main']['temp']) - 273.15)
temp_feels=  ((api_data['main']['feels_like']) - 273.15)
temp_maximum= ((api_data['main']['temp_max']) - 273.15)
temp_minimum= ((api_data['main']['temp_min']) - 273.15)
preasure = ((api_data['main']['temp_min'])/10)
humidity = api_data['main']['humidity']

#Report on Wearther.
weather_description = api_data['weather'][0]['description']
weather = api_data['weather'][0]['main']
windspeed = api_data['wind']['speed']

#Country With Corrdinates
dateandtime =datetime.now().strftime("%d %b %Y Time: %I:%M:%S %p")
country= api_data['sys']['country']
cord_long=api_data['coord']['lon']
cord_lat=api_data['coord']['lat']


#Terminal Print
print ("===============================================================================================================")
print ("         Weather Report Using Python | Report of - {}  || Dated :{}".format(location.upper(), dateandtime)) 
print ("--------------------------------------------------------------------------------------------------------------")
print("          .........................        General Informations ...........................")
print("")
print(" 	Town or Place		:",location)
print(" 	Country			:",country)
print(" 	Longitude		:",cord_long)
print(" 	Latitude		:",cord_lat)
print(" 	Current Date and Time 	: ",dateandtime)
print("")
print("          .........................        Weather Informations ...........................")
print("")
print ("	Current Temperature is 	: {:.2f} deg C".format(temperature))
print ("	Feels Like 		: {:.2f} deg C".format(temp_feels))
print ("	Maximum Temperature 	: {:.2f} deg C".format(temp_maximum))
print ("	Minimum Temperature 	: {:.2f} deg C".format(temp_minimum))
print ("	Current weather desc  	:",weather_description)
print ("	Current weather 	:",weather)
print ("	Current Humidity      	:",humidity, '%')
print ("	Current Preasure	: {:.2f} Hg".format(preasure))
print ("	Current wind speed    	:",windspeed ,'kmph')
print("")
print ("===============================================================================================================")

#Saving  in a Log File.
filename=location
filenamefinal = "%s.txt" % filename
with open(filenamefinal, 'w',) as f:
	f.write("===============================================================================================================\n")
	f.write("	Weather Report Using Python | Report of - {}  || Dated :{}".format(location.upper(), dateandtime))	
	f.write("\n--------------------------------------------------------------------------------------------------------------\n")
	f.write("           .............................General Informations ...........................\n")
	f.write("\n")
	f.write("			Town or Place		:{}".format(location.upper()))
	f.write("\n")
	f.write("			Country		 	:{}".format(country.upper()))
	f.write("\n") 
	f.write("			Longitude	 	:{}".format(cord_long))
	f.write("\n")
	f.write("			Latitude	 	:{}".format(cord_lat))
	f.write("\n")
	f.write("			Current Date and Time	:{}".format(dateandtime))
	f.write("\n")
	f.write("           .............................Weather Informations ...........................\n")
	f.write("\n")
	f.write("			Current Temperature is	 :{:.2f} deg C".format(temperature))
	f.write("\n")
	f.write("			Feels Like		 :{:.2f} deg C".format(temp_feels))
	f.write("\n") 
	f.write("			Maximum Temperature	 :{:.2f} deg C".format(temp_maximum))
	f.write("\n")
	f.write("			Minimum Temperature	 :{:.2f} deg C".format(temp_minimum))
	f.write("\n")
	f.write("			Current weather desc	 :{}".format(weather_description.upper()))
	f.write("\n")
	f.write("			Current weather		 :{}".format(weather.upper()))
	f.write("\n")
	f.write("			Current Humidity	 :{}".format(humidity))
	f.write("%")
	f.write("\n") 
	f.write("			Current Preasure	 :{:.2f} Hg".format(preasure))
	f.write("\n")
	f.write("			Current wind speed	 :{}".format(humidity))
	f.write("kmph")
	f.write("\n")
	f.write("           ............................. End of Report.. ...........................\n")
	f.write("\n")
	f.write("\n")
	f.write(" 															Written By Anjana T A |ShapeAI Project |Weather and Python   ")

#Code Done By Anjana T A
#Email Address: anjanata99@gmail.com 
#Python And Cyber Security Bootcamp Project