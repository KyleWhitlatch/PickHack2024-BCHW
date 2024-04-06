############################################################################################################

# Importing the necessary libraries
import psutil
import cpuinfo
import subprocess
import class_info

system = class_info.info()

system.get_all_information()
system.parse_all_information()
system.print_all_information()

############################################################################################################