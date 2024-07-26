from UNIT_library import UNIT
import socket
from datetime import datetime
import time 
import traceback
import sys
import os

# Asyncua stuff
import asyncio
from asyncua import ua, Server


class UPS(UNIT):
    '''
    This class represents the template to
    monitor an UPS system.
    '''
    def __init__(self,ip):
        UPS_MIBS=os.getenv('UPS_MIB_DIR')
        self.mib_dir = UPS_MIBS   # Need to declare a top directory for this 
        self.device_address = ip #"192.168.197.92"
        self.GLOBAL_MIBS=os.getenv('GLOBAL_MIB_DIR')

    def get_battery_fail(self):
        ups_stat_var = "xupsBatteryFailure.0"
        command = f"snmpget -v 3 -M {self.mib_dir} -M +{self.GLOBAL_MIBS} -m ALL -u readonly -c public {self.device_address} {ups_stat_var}" 
        output_command = self.execute_command(command)
        temp_val = self.parse_snmpget_output(output_command)
        return temp_val['Value']
    
    def get_battery_time(self):
        ups_stat_var = "xupsBatTimeRemaining.0"
        command = f"snmpget -v 3 -M {self.mib_dir} -M +{self.GLOBAL_MIBS} -m ALL -u readonly -c public {self.device_address} {ups_stat_var}" 
        output_command = self.execute_command(command)
        temp_val = self.parse_snmpget_output(output_command)
        return temp_val['Value']
    
    def get_battery_cap(self):
        ups_stat_var = "xupsBatCapacity.0"
        command = f"snmpget -v 3 -M {self.mib_dir} -M +{self.GLOBAL_MIBS} -m ALL -u readonly -c public {self.device_address} {ups_stat_var}" 
        output_command = self.execute_command(command)
        temp_val = self.parse_snmpget_output(output_command)
        return temp_val['Value']
    
    def get_battery_voltage(self):
        ups_stat_var = "xupsBatVoltage.0"
        command = f"snmpget -v 3 -M {self.mib_dir} -M +{self.GLOBAL_MIBS} -m ALL -u readonly -c public {self.device_address} {ups_stat_var}" 
        output_command = self.execute_command(command)
        temp_val = self.parse_snmpget_output(output_command)
        return temp_val['Value']
    
    def get_battery_age(self):
        ups_stat_var = "xupsBatteryAged.0"
        command = f"snmpget -v 3 -M {self.mib_dir} -M +{self.GLOBAL_MIBS} -m ALL -u readonly -c public {self.device_address} {ups_stat_var}" 
        output_command = self.execute_command(command)
        temp_val = self.parse_snmpget_output(output_command)
        return temp_val['Value']
    

if __name__ == "__main__":
    ups_a = UPS("192.168.197.92")
    print(ups_a.get_battery_fail())
    print(ups_a.get_battery_cap())
    print(ups_a.get_battery_age())
    print(ups_a.get_battery_voltage())
    print(ups_a.get_battery_time())




