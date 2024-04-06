############################################################################################################

# Importing the necessary libraries
import psutil
import cpuinfo
import subprocess
import hashlib
from web3 import Web3
import class_info



system = class_info.info()

system.get_all_information()
system.parse_all_information()
# system.print_all_information()

# print(system.hash_with_keccak())

system.get_using_vars()
system.parse_using_vars()
system.print_using_vars()
   
############################################################################################################