'''
APPLICATION FOR BCHW VERIFICATION

'''

'''
# About the application

This part of the application will get the specific system identifiers including but not limited to:
cpu, memory, disk, network, and other system information. 
The application will then send the information to the server for verification. 
The server will then verify the information and send back a response to the client. 
The client will then display the response to the user.

'''

# Importing the necessary libraries
import psutil
import cpuinfo
import subprocess

############################################################################################################

# CPU variables list
cpu_vars = ['AddressWidth', 'Architecture', 'AssetTag', 'Availability', 'Caption', 'Characteristics', 'ConfigManagerErrorCode', 'ConfigManagerUserConfig', 'CpuStatus', 'CreationClassName', 'CurrentClockSpeed', 'CurrentVoltage', 'DataWidth', 'Description', 'DeviceID', 'ErrorCleared', 'ErrorDescription', 'ExtClock', 'Family', 'InstallDate', 'L2CacheSize', 'L2CacheSpeed', 'L3CacheSize', 'L3CacheSpeed', 'LastErrorCode', 'Level', 'LoadPercentage', 'Manufacturer', 'MaxClockSpeed', 'Name', 'NumberOfCores', 'NumberOfEnabledCore', 'NumberOfLogicalProcessors', 'OtherFamilyDescription', 'PartNumber', 'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'ProcessorId', 'ProcessorType', 'Revision', 'Role', 'SecondLevelAddressTranslationExtensions', 'SerialNumber', 'SocketDesignation', 'Status', 'StatusInfo', 'Stepping', 'SystemCreationClassName', 'SystemName', 'ThreadCount', 'UniqueId', 'UpgradeMethod', 'Version', 'VirtualizationFirmwareEnabled', 'VMMonitorModeExtensions', 'VoltageCaps']
full_cpu_information = []

# Memory variables list
ram_vars = ['AdminPasswordStatus', 'AutomaticManagedPagefile', 'AutomaticResetBootOption', 'AutomaticResetCapability', 'BootOptionOnLimit', 'BootOptionOnWatchDog', 'BootROMSupported', 'BootStatus', 'BootupState', 'Caption', 'ChassisBootupState', 'ChassisSKUNumber', 'CreationClassName', 'CurrentTimeZone', 'DaylightInEffect', 'Description', 'DNSHostName', 'Domain', 'DomainRole', 'EnableDaylightSavingsTime', 'FrontPanelResetStatus', 'HypervisorPresent', 'InfraredSupported', 'InitialLoadInfo', 'InstallDate', 'KeyboardPasswordStatus', 'LastLoadInfo', 'Manufacturer', 'Model', 'Name', 'NameFormat', 'NetworkServerModeEnabled', 'NumberOfLogicalProcessors', 'NumberOfProcessors', 'OEMLogoBitmap', 'OEMStringArray', 'PartOfDomain', 'PauseAfterReset', 'PCSystemType', 'PCSystemTypeEx', 'PowerManagementCapabilities', 'PowerManagementSupported', 'PowerOnPasswordStatus', 'PowerState', 'PowerSupplyState', 'PrimaryOwnerContact', 'PrimaryOwnerName', 'ResetCapability', 'ResetCount', 'ResetLimit', 'Roles', 'Status', 'SupportContactDescription', 'SystemFamily', 'SystemSKUNumber', 'SystemStartupDelay', 'SystemStartupOptions', 'SystemStartupSetting', 'SystemType', 'ThermalState', 'TotalPhysicalMemory', 'UserName', 'WakeUpType', 'Workgroup']
full_ram_information = []

# Disk variables list
disk_vars = ['Availability', 'BytesPerSector', 'Capabilities', 'CapabilityDescriptions', 'Caption', 'CompressionMethod', 'ConfigManagerErrorCode', 'ConfigManagerUserConfig', 'CreationClassName', 'DefaultBlockSize', 'Description', 'DeviceID', 'ErrorCleared', 'ErrorDescription', 'ErrorMethodology', 'FirmwareRevision', 'Index', 'InstallDate', 'InterfaceType', 'LastErrorCode', 'Manufacturer', 'MaxBlockSize', 'MaxMediaSize', 'MediaLoaded', 'MediaType', 'MinBlockSize', 'Model', 'Name', 'NeedsCleaning', 'NumberOfMediaSupported', 'Partitions', 'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'SCSIBus', 'SCSILogicalUnit', 'SCSIPort', 'SCSITargetId', 'SectorsPerTrack', 'SerialNumber', 'Signature', 'Size', 'Status', 'StatusInfo', 'SystemCreationClassName', 'SystemName', 'TotalCylinders', 'TotalHeads', 'TotalSectors', 'TotalTracks', 'TracksPerCylinder']
full_disk_information = []

# Network variables list
network_vars = ['AdapterType', 'AdapterTypeId', 'AutoSense', 'Availability', 'Caption', 'ConfigManagerErrorCode', 'ConfigManagerUserConfig', 'CreationClassName', 'Description', 'DeviceID', 'ErrorCleared', 'ErrorDescription', 'GUID', 'Index', 'InstallDate', 'Installed', 'InterfaceIndex', 'LastErrorCode', 'MACAddress', 'Manufacturer', 'MaxNumberControlled', 'MaxSpeed', 'Name', 'NetConnectionID', 'NetConnectionStatus', 'NetEnabled', 'NetworkAddresses', 'PermanentAddress', 'PhysicalAdapter', 'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'ProductName', 'ServiceName', 'Speed', 'Status', 'StatusInfo', 'SystemCreationClassName', 'SystemName', 'TimeOfLastReset']
full_network_information = []

# Motherboard variables list
motherboard_vars = ['Caption', 'ConfigOptions', 'CreationClassName', 'Depth', 'Description', 'Height', 'HostingBoard', 'HotSwappable', 'InstallDate', 'Manufacturer', 'Model', 'Name', 'OtherIdentifyingInfo', 'PartNumber', 'PoweredOn', 'Product', 'Removable', 'Replaceable', 'RequirementsDescription', 'RequiresDaughterBoard', 'SerialNumber', 'SKU', 'SlotLayout', 'SpecialRequirements', 'Status', 'Tag', 'Version', 'Weight', 'Width']
full_motherboard_information = []

############################################################################################################

## WORKS
# Get CPU information
cpu_info = cpuinfo.get_cpu_info()
cpu_percent = psutil.cpu_percent(interval=1)

def get_cpu_information(cpu_vars):
    for var in cpu_vars:
        full_cpu_information.append(subprocess.check_output(['wmic', 'cpu', 'get', var]).decode())
        
def parse_cpu_information(full_cpu_information):
    for i in range(len(full_cpu_information)):
        full_cpu_information[i] = full_cpu_information[i].split('\n')[1].strip()

def print_full_cpu_information(full_cpu_information):
    for i in range(len(full_cpu_information)):
        print(f"{cpu_vars[i]}: {full_cpu_information[i]}")

# get_cpu_information(cpu_vars)
# parse_cpu_information(full_cpu_information)
# print_full_cpu_information(full_cpu_information)

############################################################################################################

## WORKS
# Get memory information
memory_info = psutil.virtual_memory()

# Get RAM information
def get_ram_information(ram_vars):
    for var in ram_vars:
        full_ram_information.append(subprocess.check_output(['wmic', 'COMPUTERSYSTEM', 'get', var]).decode())
    
def parse_ram_information(full_ram_information):
    for i in range(len(full_ram_information)):
        full_ram_information[i] = full_ram_information[i].split('\n')[1].strip()

def print_full_ram_information(full_ram_information):
    for i in range(len(full_ram_information)):
        print(f"{ram_vars[i]}: {full_ram_information[i]}")
        
# get_ram_information(ram_vars)
# parse_ram_information(full_ram_information)
# print_full_ram_information(full_ram_information)

############################################################################################################

## WORKS
# Get disk information
disk_usage = psutil.disk_usage('/')

def get_disk_information(disk_vars):
    for var in disk_vars:
        full_disk_information.append(subprocess.check_output(['wmic', 'diskdrive', 'get', var]).decode())
        
def parse_disk_information(full_disk_information):
    for i in range(len(full_disk_information)):
        full_disk_information[i] = full_disk_information[i].split('\n')[1].strip()

def print_full_disk_information(full_disk_information):
    for i in range(len(full_disk_information)):
        print(f"{disk_vars[i]}: {full_disk_information[i]}")

# get_disk_information(disk_vars)
# parse_disk_information(full_disk_information)
# print_full_disk_information(full_disk_information)

############################################################################################################

## WORKS
# Get network information
network_info = psutil.net_io_counters()

# network_information_test = subprocess.check_output(['wmic', 'nic', 'get']).decode()
# print(network_information_test)

def get_network_information(network_vars):
    for var in network_vars:
        full_network_information.append(subprocess.check_output(['wmic', 'nic', 'get', var]).decode())

def parse_network_information(full_network_information):
    for i in range(len(full_network_information)):
        full_network_information[i] = full_network_information[i].split('\n')[1].strip()

def print_full_network_information(full_network_information):
    for i in range(len(full_network_information)):
        print(f"{network_vars[i]}: {full_network_information[i]}")

# get_network_information(network_vars)
# parse_network_information(full_network_information)
# print_full_network_information(full_network_information)

############################################################################################################

## WORKS
# Get Motherboard information

# motherboard_info = subprocess.check_output(['wmic', 'baseboard', 'get']).decode()
# print(motherboard_info)

def get_motherboard_information(motherboard_vars):
    for var in motherboard_vars:
        full_motherboard_information.append(subprocess.check_output(['wmic', 'baseboard', 'get', var]).decode())

def parse_motherboard_information(full_motherboard_information):
    for i in range(len(full_motherboard_information)):
        full_motherboard_information[i] = full_motherboard_information[i].split('\n')[1].strip()

def print_full_motherboard_information(full_motherboard_information):
    for i in range(len(full_motherboard_information)):
        print(f"{motherboard_vars[i]}: {full_motherboard_information[i]}")
        
# get_motherboard_information(motherboard_vars)
# parse_motherboard_information(full_motherboard_information)
# print_full_motherboard_information(full_motherboard_information)

############################################################################################################
'''
print("System Information: ")
print("=====================================")

print("cpu_info: ")

get_cpu_information(cpu_vars)
parse_cpu_information(full_cpu_information)
print_full_cpu_information(full_cpu_information)

print()
print("=====================================")

print("memory_info: ")

get_ram_information(ram_vars)
parse_ram_information(full_ram_information)
print_full_ram_information(full_ram_information)

print()
print("=====================================")

print("disk_usage: ")

get_disk_information(disk_vars)
parse_disk_information(full_disk_information)
print_full_disk_information(full_disk_information)

print()
print("=====================================")

print("network_info: ")

get_network_information(network_vars)
parse_network_information(full_network_information)
print_full_network_information(full_network_information)

print()
print("=====================================")

print("motherboard_info: ")

get_motherboard_information(motherboard_vars)
parse_motherboard_information(full_motherboard_information)
print_full_motherboard_information(full_motherboard_information)
print("=====================================")
'''