#!/usr/bin/env python

from __future__ import print_function
import iscpy, sys

try:
    # Read in an existing config file
    if(sys.argv[1] == '-'):
        with sys.stdin as input_config_file:
            config_string = input_config_file.read()
    else:
	with open(sys.argv[1]) as input_config_file:
            config_string = input_config_file.read()
except:
     print("file not found or not specified")
     quit(1)


config_dict = iscpy.ParseISCString(config_string)

try:
    search=sys.argv[2]
except:
    search=None

for zone in config_dict:
    if(zone.startswith("zone")):
        zone_name = zone[zone.find('"')+1:zone.rfind('"')]
        zone_type = config_dict[zone]['type']
        zone_file = config_dict[zone]['file']
        zone_file = zone_file[zone_file.find('"')+1:zone_file.rfind('"')]

        if(search==None) or (zone_type==search):
            print (zone_type, zone_name, zone_file, sep='|')
