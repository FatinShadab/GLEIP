r"""gle_ip_info is a simple custom library for retrive local_ip/global_ip/external_ip address as string.

It use's -->

    --> os module,
    --> requests module,
    --> platfrom module,
    --> upnpclient module.

***Local_IP is collected from the cmd(in Windows) or Bash-Terminal(in Linux) using 'ipconfig'/ 
'hostname -I' command.So there is no need to get the hostname like socket module does and 
the accuracy of the output is 100% in Linux Os.

***Global_IP is collected by sending request to 'https://checkip.amazonaws.com' or 
'https://www.wikipedia.org' using python requests module.So to get the global_ip a stable 
net connection is needed.

***External_IP  of any router or alike devices can be collected using upnpclient module.
It takes a little more time to get the external_ipaddress Compare to other two functions.Though it don't require
stable Internet connection but requires a stable connection between the devices.

sample code ==>

from gle_ip_info import IP

Ip = IP()

# TO get your local ipaddress.
local_ip = Ip.get_local_ip() 

# To get your global ipaddress.
global_ip = Ip.get_global_ip()

# To get external(of connected device) ipaddress.
external_ip = Ip.get_external_ip() # returns the ip address of 1st device
"""

__author__ = "Fastin Shadab"
__email__ = "fatinshadab123@gmail.com"
__status__ = "planning"


import os
import requests
import platform
import upnpclient


class IP:
    '''A class for retrieve ipaddress <local_ip/global_ip/external_ip_1>.(***Supported Os's are i)Windows, ii)Linux***)'''
    def __init__(self):
        '''******'''
        self.custom_ip_Error = ''  
        self.Os = platform.system()
        self.Os_tuple = ('Windows', 'Linux')
        self.devices = upnpclient.discover()
        self.urls = ('https://checkip.amazonaws.com', 'https://www.wikipedia.org')

        try:
            if self.Os == self.Os_tuple[0]:
                self.stream = os.popen('ipconfig')
            if self.Os == self.Os_tuple[1]:
                self.stream = os.popen('hostname -I')
        except:
            self.custom_ip_Error = f"{platform.system()} is't supported. (***Supported Os's are i)Windows, ii)Linux***)"
            return self.custom_ip_Error

    def preprocessed_data_win(self):
        '''A function to retrieve ipaddress from <os._wrap_close object> as str (***if os is win32/64***)'''
        data = self.stream.readlines()

        dict = {}
        for index, line in enumerate(data):
            dict[index] = line

        raw_ip_str = dict[23]
        ip_list = list(raw_ip_str)
        ip_addrs = ip_list[39:(len(ip_list)-1)]
        ip = ('{}'*len(ip_addrs)).format(*ip_addrs)
    
        return ip

    def preprocessed_data_linux(self):
        '''A function to retrieve ipaddress from <os._wrap_close object> as str (***if os is linux***)'''
        data = self.stream.read()
        ip = str(data)

        return ip

    def get_local_ip(self):
        '''Os independent function for retrieve local ipaddress.'''
        try:
            if self.Os == self.Os_tuple[0]:
                return self.preprocessed_data_win()
            if self.Os == self.Os_tuple[1]:
                return self.preprocessed_data_linux()
        except:
            return self.custom_ip_Error

    def get_global_ip(self):
        '''Function to retrieve global ipaddress.'''
        try:
            try:
                global_ip = requests.get(self.urls[0]).text.strip()
            except:
                global_ip = requests.get(self.urls[1].headers['X-Client-IP'])
        except AttributeError as e:
            self.custom_ip_Error = 'No Internet Connection!(***Internet Connection Required***)'
            return self.custom_ip_Error

        return global_ip

    def get_external_ip(self, device_No=0):
        '''Function for retrieve connected device's external IpAddress.'''
        try:
            if(len(self.devices) > 0):
                externalIP = self.devices[device_No].WANIPConn1.GetExternalIPAddress()
        except:
            self.custom_ip_Error = "No Device's <router> are connected!"
            return self.custom_ip_Error

        return externalIP['NewExternalIPAddress']