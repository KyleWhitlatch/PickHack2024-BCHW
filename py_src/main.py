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

# DeviceID: This is a unique identifier for the device.
# L2CacheSize: This indicates the size of the level 2 cache and won't change unless the hardware is physically modified.
# L3CacheSize: This indicates the size of the level 3 cache and won't change unless the hardware is physically modified.
# Manufacturer: This indicates the manufacturer of the processor and won't change.
# Name: This indicates the name of the processor and won't change.
# NumberOfCores: This indicates the number of cores in the processor and won't change unless the hardware is physically modified.
# NumberOfEnabledCore: This indicates the number of enabled cores in the processor and won't change unless the hardware is physically modified.
# NumberOfLogicalProcessors: This indicates the number of logical processors and won't change unless the hardware is physically modified.
# ProcessorId: This is a unique identifier for the processor.
# SocketDesignation: This indicates the socket or slot where the processor is installed and won't change unless the hardware is physically modified.
# SystemName: This is the name of the computer system and won't change unless it's manually changed by the user.

full_cpu_vars = ['AddressWidth', 'Architecture', 'AssetTag', 'Availability', 'Caption', 'Characteristics', 'ConfigManagerErrorCode', 'ConfigManagerUserConfig', 'CpuStatus', 'CreationClassName', 'CurrentClockSpeed', 'CurrentVoltage', 'DataWidth', 'Description', 'DeviceID', 'ErrorCleared', 'ErrorDescription', 'ExtClock', 'Family', 'InstallDate', 'L2CacheSize', 'L2CacheSpeed', 'L3CacheSize', 'L3CacheSpeed', 'LastErrorCode', 'Level', 'LoadPercentage', 'Manufacturer', 'MaxClockSpeed', 'Name', 'NumberOfCores', 'NumberOfEnabledCore', 'NumberOfLogicalProcessors', 'OtherFamilyDescription', 'PartNumber', 'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'ProcessorId', 'ProcessorType', 'Revision', 'Role', 'SecondLevelAddressTranslationExtensions', 'SerialNumber', 'SocketDesignation', 'Status', 'StatusInfo', 'Stepping', 'SystemCreationClassName', 'SystemName', 'ThreadCount', 'UniqueId', 'UpgradeMethod', 'Version', 'VirtualizationFirmwareEnabled', 'VMMonitorModeExtensions', 'VoltageCaps']
cpu_vars = ['DeviceID', 'L2CacheSize', 'L3CacheSize', 'Manufacturer', 'Name', 'NumberOfCores', 'NumberOfEnabledCore', 'NumberOfLogicalProcessors', 'ProcessorId', 'SocketDesignation', 'SystemName']
full_cpu_information = []

# Memory variables list

# Manufacturer: This indicates the manufacturer of the system and won't change.
# Model: This indicates the model of the system and won't change.
# Name: This is the name of the computer system and won't change unless it's manually changed by the user.
# NumberOfLogicalProcessors: This indicates the number of logical processors and won't change unless the hardware is physically modified.
# NumberOfProcessors: This indicates the number of processors and won't change unless the hardware is physically modified.
# SystemFamily: This indicates the family of the system and won't change.
# SystemSKUNumber: This is a unique identifier for the system and won't change.
# SystemType: This indicates the type of system and won't change.
# TotalPhysicalMemory: This indicates the total physical memory and won't change unless the hardware is physically modified.

full_ram_vars = ['AdminPasswordStatus', 'AutomaticManagedPagefile', 'AutomaticResetBootOption', 'AutomaticResetCapability', 'BootOptionOnLimit', 'BootOptionOnWatchDog', 'BootROMSupported', 'BootStatus', 'BootupState', 'Caption', 'ChassisBootupState', 'ChassisSKUNumber', 'CreationClassName', 'CurrentTimeZone', 'DaylightInEffect', 'Description', 'DNSHostName', 'Domain', 'DomainRole', 'EnableDaylightSavingsTime', 'FrontPanelResetStatus', 'HypervisorPresent', 'InfraredSupported', 'InitialLoadInfo', 'InstallDate', 'KeyboardPasswordStatus', 'LastLoadInfo', 'Manufacturer', 'Model', 'Name', 'NameFormat', 'NetworkServerModeEnabled', 'NumberOfLogicalProcessors', 'NumberOfProcessors', 'OEMLogoBitmap', 'OEMStringArray', 'PartOfDomain', 'PauseAfterReset', 'PCSystemType', 'PCSystemTypeEx', 'PowerManagementCapabilities', 'PowerManagementSupported', 'PowerOnPasswordStatus', 'PowerState', 'PowerSupplyState', 'PrimaryOwnerContact', 'PrimaryOwnerName', 'ResetCapability', 'ResetCount', 'ResetLimit', 'Roles', 'Status', 'SupportContactDescription', 'SystemFamily', 'SystemSKUNumber', 'SystemStartupDelay', 'SystemStartupOptions', 'SystemStartupSetting', 'SystemType', 'ThermalState', 'TotalPhysicalMemory', 'UserName', 'WakeUpType', 'Workgroup']
ram_vars = ['Manufacturer', 'Model', 'Name', 'NumberOfLogicalProcessors', 'NumberOfProcessors', 'SystemFamily', 'SystemSKUNumber', 'SystemType', 'TotalPhysicalMemory']
full_ram_information = []

# Disk variables list

# DeviceID: This is a unique identifier for the disk drive.
# FirmwareRevision: This indicates the firmware revision of the disk drive and won't change unless the firmware is updated.
# Model: This indicates the model of the disk drive and won't change.
# Name: This is the name of the disk drive and won't change unless it's manually changed by the user.
# PNPDeviceID: This is a unique identifier for the disk drive.
# SerialNumber: This is a unique identifier for the disk drive.
# Size: This indicates the size of the disk drive and won't change unless the hardware is physically modified.
# SystemName: This is the name of the computer system and won't change unless it's manually changed by the user.

full_disk_vars = ['Availability', 'BytesPerSector', 'Capabilities', 'CapabilityDescriptions', 'Caption', 'CompressionMethod', 'ConfigManagerErrorCode', 'ConfigManagerUserConfig', 'CreationClassName', 'DefaultBlockSize', 'Description', 'DeviceID', 'ErrorCleared', 'ErrorDescription', 'ErrorMethodology', 'FirmwareRevision', 'Index', 'InstallDate', 'InterfaceType', 'LastErrorCode', 'Manufacturer', 'MaxBlockSize', 'MaxMediaSize', 'MediaLoaded', 'MediaType', 'MinBlockSize', 'Model', 'Name', 'NeedsCleaning', 'NumberOfMediaSupported', 'Partitions', 'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'SCSIBus', 'SCSILogicalUnit', 'SCSIPort', 'SCSITargetId', 'SectorsPerTrack', 'SerialNumber', 'Signature', 'Size', 'Status', 'StatusInfo', 'SystemCreationClassName', 'SystemName', 'TotalCylinders', 'TotalHeads', 'TotalSectors', 'TotalTracks', 'TracksPerCylinder']
disk_vars = ['DeviceID', 'FirmwareRevision', 'Model', 'Name', 'PNPDeviceID', 'SerialNumber', 'Size', 'SystemName']
full_disk_information = []

# Network variables list

# DeviceID: This is a unique identifier for the network adapter.
# Name: This is the name of the network adapter and won't change unless it's manually changed by the user.
# PNPDeviceID: This is a unique identifier for the network adapter.
# ProductName: This indicates the product name of the network adapter and won't change.
# ServiceName: This indicates the service name of the network adapter and won't change.
# SystemName: This is the name of the computer system and won't change unless it's manually changed by the user.

full_network_vars = ['AdapterType', 'AdapterTypeId', 'AutoSense', 'Availability', 'Caption', 'ConfigManagerErrorCode', 'ConfigManagerUserConfig', 'CreationClassName', 'Description', 'DeviceID', 'ErrorCleared', 'ErrorDescription', 'GUID', 'Index', 'InstallDate', 'Installed', 'InterfaceIndex', 'LastErrorCode', 'MACAddress', 'Manufacturer', 'MaxNumberControlled', 'MaxSpeed', 'Name', 'NetConnectionID', 'NetConnectionStatus', 'NetEnabled', 'NetworkAddresses', 'PermanentAddress', 'PhysicalAdapter', 'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'ProductName', 'ServiceName', 'Speed', 'Status', 'StatusInfo', 'SystemCreationClassName', 'SystemName', 'TimeOfLastReset']
network_vars = ['DeviceID', 'Name', 'PNPDeviceID', 'ProductName', 'ServiceName', 'SystemName']
full_network_information = []

# Motherboard variables list

# Manufacturer: This indicates the manufacturer of the motherboard and won't change.
# Name: This is the name of the motherboard and won't change unless it's manually changed by the user.
# Product: This indicates the product name of the motherboard and won't change.
# SerialNumber: This is a unique identifier for the motherboard.
# Tag: This is a tag for the motherboard and won't change unless it's manually changed by the user.
# Version: This indicates the version of the motherboard and won't change unless the hardware is physically modified.

full_motherboard_vars = ['Caption', 'ConfigOptions', 'CreationClassName', 'Depth', 'Description', 'Height', 'HostingBoard', 'HotSwappable', 'InstallDate', 'Manufacturer', 'Model', 'Name', 'OtherIdentifyingInfo', 'PartNumber', 'PoweredOn', 'Product', 'Removable', 'Replaceable', 'RequirementsDescription', 'RequiresDaughterBoard', 'SerialNumber', 'SKU', 'SlotLayout', 'SpecialRequirements', 'Status', 'Tag', 'Version', 'Weight', 'Width']
motherboard_vars = ['Manufacturer', 'Name', 'Product', 'SerialNumber', 'Tag', 'Version']
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
    i = 0
    while i < len(full_cpu_information):
        info = full_cpu_information[i].split('\n')[1].strip()
        if info:
            full_cpu_information[i] = info
            i += 1
        else:
            del full_cpu_information[i]
            del cpu_vars[i]

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
    i = 0
    while i < len(full_ram_information):
        info = full_ram_information[i].split('\n')[1].strip()
        if info:
            full_ram_information[i] = info
            i += 1
        else:
            del full_ram_information[i]
            del ram_vars[i]

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
    i= 0
    while i < len(full_disk_information):
        info = full_disk_information[i].split('\n')[1].strip()
        if info:
            full_disk_information[i] = info
            i += 1
        else:
            del full_disk_information[i]
            del disk_vars[i]

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
    i = 0
    while i < len(full_network_information):
        info = full_network_information[i].split('\n')[1].strip()
        if info:
            full_network_information[i] = info
            i += 1
        else:
            del full_network_information[i]
            del network_vars[i]

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
    i = 0
    while i < len(full_motherboard_information):
        info = full_motherboard_information[i].split('\n')[1].strip()
        if info:
            full_motherboard_information[i] = info
            i += 1
        else:
            del full_motherboard_information[i]
            del motherboard_vars[i]

def print_full_motherboard_information(full_motherboard_information):
    for i in range(len(full_motherboard_information)):
        print(f"{motherboard_vars[i]}: {full_motherboard_information[i]}")
        
# get_motherboard_information(motherboard_vars)
# parse_motherboard_information(full_motherboard_information)
# print_full_motherboard_information(full_motherboard_information)

############################################################################################################

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
