'''
 * IP2Location C library is distributed under MIT license
 * Copyright (c) 2013-2021 IP2Location.com. support@ip2location.com
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the MIT license
'''

from ctypes import *
from ctypes.util import find_library
import sys

class IP2Location_lookup_mode :
    IP2LOCATION_FILE_IO = 0
    IP2LOCATION_CACHE_MEMORY = 1
    IP2LOCATION_SHARED_MEMORY = 2


class C_IP2LocationRecord(Structure):
    '''
        Define the IP2Location Record result structure.
    '''
    _fields_=[("country_short",c_char_p),("country_long",c_char_p),("region",c_char_p),("city",c_char_p),("isp",c_char_p),("latitude",c_float),("longitude",c_float),("domain",c_char_p),("zipcode",c_char_p),("timezone",c_char_p),("netspeed",c_char_p),("idd_code",c_char_p),("area_code",c_char_p),("weather_code",c_char_p),("weather_name",c_char_p),("mcc",c_char_p),("mnc",c_char_p),("mobile_brand",c_char_p),("elevation",c_float),("usage_type",c_char_p),("address_type",c_char_p),("category",c_char_p)]


class IP2LocationRecord:
    ''' IP2Location record with all fields from the database '''
    ip = None
    country_short = None
    country_long = None
    region = None
    city = None
    isp = None
    latitude = None
    longitude = None
    domain = None
    zipcode = None
    timezone = None
    netspeed = None
    idd_code = None
    area_code = None
    weather_code = None
    weather_name = None
    mcc = None
    mnc = None
    mobile_brand = None
    elevation = None
    usage_type = None
    address_type = None
    category = None


class IP2Location(object):

    def __init__(self, filename=None, libraryname = None):
            '''
                - Load the IP2Location C Library by using Ctypes CDLL module. If user did not pass the library name and path then this library will look for the default location of IP2Location C Library.
                - Creates a database object and opens a file if filename is given
            '''
            if filename:
                self.open(filename)
            if libraryname:
                self.load(libraryname)
            else:
                self.ip2location_c = CDLL(find_library('IP2Location'))

    def load(self, libraryname):
        '''
            Function to load the IP2Location C Library if user choose to load their own copy of IP2Location C Library.
        '''
        self.ip2location_c = CDLL(libraryname)

    def open(self, filename, mode=None):
        ''' 
            Function to pass the database name and path to IP2Location_open in IP2Location C library.
            Set the argument and response types of the function to avoid data compatibility issue. 
        '''
        if (mode == None):
            mode = IP2Location_lookup_mode.IP2LOCATION_FILE_IO
        self.ip2location_c.IP2Location_open.argtypes = [c_char_p]
        self.ip2location_c.IP2Location_open.restype = c_void_p
        self.ip2location_c.IP2Location_open_mem.argtypes = [c_void_p, c_int]
        # self.ip2location_database_pointer = self.ip2location_c.IP2Location_open(filename)
        if sys.version < '3':
            self.ip2location_database_pointer = self.ip2location_c.IP2Location_open(filename)
        else:
            self.ip2location_database_pointer = self.ip2location_c.IP2Location_open(bytes(filename, encoding='utf-8'))
        self.ip2location_c.IP2Location_open_mem(self.ip2location_database_pointer, mode)

    def get_country_short(self, ip):
        ''' Get country_short '''
        rec = self.get_all(ip)
        return rec and rec.country_short
    def get_country_long(self, ip):
        ''' Get country_long '''
        rec = self.get_all(ip)
        return rec and rec.country_long
    def get_region(self, ip):
        ''' Get region '''
        rec = self.get_all(ip)
        return rec and rec.region
    def get_city(self, ip):
        ''' Get city '''
        rec = self.get_all(ip)
        return rec and rec.city
    def get_isp(self, ip):
        ''' Get isp '''
        rec = self.get_all(ip)
        return rec and rec.isp
    def get_latitude(self, ip):
        ''' Get latitude '''
        rec = self.get_all(ip)
        return rec and rec.latitude
    def get_longitude(self, ip):
        ''' Get longitude '''
        rec = self.get_all(ip)
        return rec and rec.longitude
    def get_domain(self, ip):
        ''' Get domain '''
        rec = self.get_all(ip)
        return rec and rec.domain
    def get_zipcode(self, ip):
        ''' Get zipcode '''
        rec = self.get_all(ip)
        return rec and rec.zipcode
    def get_timezone(self, ip):
        ''' Get timezone '''
        rec = self.get_all(ip)
        return rec and rec.timezone
    def get_netspeed(self, ip):
        ''' Get netspeed '''
        rec = self.get_all(ip)
        return rec and rec.netspeed
    def get_idd_code(self, ip):
        ''' Get idd_code '''
        rec = self.get_all(ip)
        return rec and rec.idd_code
    def get_area_code(self, ip):
        ''' Get area_code '''
        rec = self.get_all(ip)
        return rec and rec.area_code
    def get_weather_code(self, ip):
        ''' Get weather_code '''
        rec = self.get_all(ip)
        return rec and rec.weather_code
    def get_weather_name(self, ip):
        ''' Get weather_name '''
        rec = self.get_all(ip)
        return rec and rec.weather_name
    def get_mcc(self, ip):
        ''' Get mcc '''
        rec = self.get_all(ip)
        return rec and rec.mcc
    def get_mnc(self, ip):
        ''' Get mnc '''
        rec = self.get_all(ip)
        return rec and rec.mnc
    def get_mobile_brand(self, ip):
        ''' Get mobile_brand '''
        rec = self.get_all(ip)
        return rec and rec.mobile_brand
    def get_elevation(self, ip):
        ''' Get elevation '''
        rec = self.get_all(ip)
        return rec and rec.elevation
    def get_usage_type(self, ip):
        ''' Get usage_type '''
        rec = self.get_all(ip)
        return rec and rec.usage_type
    def get_address_type(self, ip):
        ''' Get address_type '''
        rec = self.get_all(ip)
        return rec and rec.address_type
    def get_category(self, ip):
        ''' Get category '''
        rec = self.get_all(ip)
        return rec and rec.category

    def get_all(self, ip):
        ''' set the argument and response types of the function for data compatibility issue. '''
        self.ip2location_c.IP2Location_get_all.argtypes = [c_void_p, c_char_p]
        # Need to set to the struct that created in the begining to get valid output instead of a pointer.
        self.ip2location_c.IP2Location_get_all.restype = POINTER(C_IP2LocationRecord) 
        self.rec = IP2LocationRecord()
        # self.result = self.ip2location_c.IP2Location_get_all(self.ip2location_database_pointer, ip)
        if sys.version < '3':
            self.result = self.ip2location_c.IP2Location_get_all(self.ip2location_database_pointer, ip)
        else:
            self.result = self.ip2location_c.IP2Location_get_all(self.ip2location_database_pointer, bytes(ip, encoding='utf-8'))
        self.rec.country_short = self.result.contents.country_short
        self.rec.country_long = self.result.contents.country_long
        self.rec.region = self.result.contents.region
        self.rec.city = self.result.contents.city
        self.rec.isp = self.result.contents.isp
        self.rec.latitude = self.result.contents.latitude
        self.rec.longitude = self.result.contents.longitude
        self.rec.domain = self.result.contents.domain
        self.rec.zipcode = self.result.contents.zipcode
        self.rec.timezone = self.result.contents.timezone
        self.rec.netspeed = self.result.contents.netspeed
        self.rec.idd_code = self.result.contents.idd_code
        self.rec.area_code = self.result.contents.area_code
        self.rec.weather_code = self.result.contents.weather_code
        self.rec.weather_name = self.result.contents.weather_name
        self.rec.mcc = self.result.contents.mcc
        self.rec.mnc = self.result.contents.mnc
        self.rec.mobile_brand = self.result.contents.mobile_brand
        self.rec.elevation = self.result.contents.elevation
        self.rec.usage_type = self.result.contents.usage_type
        self.rec.address_type = self.result.contents.address_type
        self.rec.category = self.result.contents.category
        return self.rec

    def close(self):
        '''
            Close the IP2Location database file.
        '''
        self.ip2location_c.IP2Location_free_record.argtypes = [POINTER(C_IP2LocationRecord)]
        self.ip2location_c.IP2Location_close.argtypes = [c_void_p]
        # Free the record object first before close the file
        self.ip2location_c.IP2Location_free_record(self.result)
        self.ip2location_c.IP2Location_close(self.ip2location_database_pointer)