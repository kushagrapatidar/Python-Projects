import phonenumbers,opencage
number=input('Enter the number: ')
from phonenumbers import geocoder,timezone,carrier
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
location=geocoder.description_for_number(phone,"en")
from opencage.geocoder import OpenCageGeocode
key="296fae6367f44c8485696aa4471ef33f"
geocoderr=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)