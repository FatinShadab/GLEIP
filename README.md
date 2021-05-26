# gleip

glip is a module for retrieve ip address like local-ip, global-ip, external-ip as string.

## Installation

Run the following to install:

'''python
pip install gle_ip
'''

## Usage
'''
from lgeip import IP

Ip = IP()

local_ip = Ip.get_local_ip() # TO get your local ipaddress.

global_ip = Ip.get_global_ip() # To get your global ipaddress.
 
external_ip = Ip.get_external_ip() # To get external(of connected device) ipaddress, returns the ip address of 1st device
'''
## How it works

It use's -->
'''
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
'''
## License

MIT License
