# Copyright (C) 2005-2019 IP2Location.com
# All Rights Reserved
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the MIT license

import os
import ip2location_python_c

ip = "8.8.8.8"

database = ip2location_python_c.IP2Location()

"""
    Cache the database into memory to accelerate lookup speed.
    WARNING: Please make sure your system have sufficient RAM to use this feature.
    Choose either one from below to load the database.
"""
# database.open(os.path.join("data", "IP2LOCATION-LITE-DB1.BIN"), ip2location_python_c.IP2Location_lookup_mode.IP2LOCATION_SHARED_MEMORY)
# database.open(os.path.join("data", "IP2LOCATION-LITE-DB1.BIN"), ip2location_python_c.IP2Location_lookup_mode.IP2LOCATION_CACHE_MEMORY)

# Load the database using FILE I/O mode.
database.open(os.path.join("data", "IP2LOCATION-LITE-DB1.BIN"))

rec = database.get_all(ip)

print("Country Code          : " + rec.country_short)
print("Country Name          : " + rec.country_long)
print("Region Name           : " + rec.region)
print("City Name             : " + rec.city)
print("ISP Name              : " + rec.isp)
print("Latitude              : " + str(rec.latitude))
print("Longitude             : " + str(rec.longitude))
print("Domain Name           : " + rec.domain)
print("ZIP Code              : " + rec.zipcode)
print("Time Zone             : " + rec.timezone)
print("Net Speed             : " + rec.netspeed)
print("Area Code             : " + rec.idd_code)
print("IDD Code              : " + rec.area_code)
print("Weather Station Code  : " + rec.weather_code)
print("Weather Station Name  : " + rec.weather_name)
print("MCC                   : " + rec.mcc)
print("MNC                   : " + rec.mnc)
print("Mobile Carrier        : " + rec.mobile_brand)
print("Elevation             : " + str(rec.elevation))
print("Usage Type            : " + rec.usage_type)
print("Address Type          : " + rec.address_type)
print("Category              : " + rec.category)
print("\nYou may download the DB25 sample BIN at https://www.ip2location.com/downloads/sample6.bin.db25.zip for full data display.")

database.close()