import phonenumbers
from phonenumbers import geocoder, carrier, timezone

num = input("Enter Phone Number (with country code, e.g. +14155552671): ")
ph = phonenumbers.parse(num)

time = timezone.time_zones_for_number(ph)
ca = carrier.name_for_number(ph, "en")
reg = geocoder.description_for_number(ph, "en")

print("Parsed Number:", ph)
print("Time Zone(s):", time)
print("Carrier:", ca)
print("Region:", reg)
