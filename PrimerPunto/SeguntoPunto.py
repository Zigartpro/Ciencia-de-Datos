from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myGeocoder_app_1")
def getStringCoordinates(var):
	if any(char.isdigit() for char in var):
		return False
	return True
def getCoordinates(city):
	try:
		location = geolocator.geocode(city)
		if location:
			print(f"{city} se encuentra en {location.address}")
		else:
			print("No se encontro la ciudad")
	except Exception as e:
		print("Error: ", e)

city_Entered = input("Ingrese la ciudad: ")
if getStringCoordinates(city_Entered):
	getCoordinates(city_Entered)
else:
	print("No puedes ingresar numeros")