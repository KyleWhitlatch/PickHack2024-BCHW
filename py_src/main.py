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
import sys
import os
import time
import psutil
import cpuinfo
import subprocess

# Memory variables list
ram_vars = ['AdminPasswordStatus', 'AutomaticManagedPagefile', 'AutomaticResetBootOption', 'AutomaticResetCapability', 'BootOptionOnLimit', 'BootOptionOnWatchDog', 'BootROMSupported', 'BootStatus', 'BootupState', 'Caption', 'ChassisBootupState', 'ChassisSKUNumber', 'CreationClassName', 'CurrentTimeZone', 'DaylightInEffect', 'Description', 'DNSHostName', 'Domain', 'DomainRole', 'EnableDaylightSavingsTime', 'FrontPanelResetStatus', 'HypervisorPresent', 'InfraredSupported', 'InitialLoadInfo', 'InstallDate', 'KeyboardPasswordStatus', 'LastLoadInfo', 'Manufacturer', 'Model', 'Name', 'NameFormat', 'NetworkServerModeEnabled', 'NumberOfLogicalProcessors', 'NumberOfProcessors', 'OEMLogoBitmap', 'OEMStringArray', 'PartOfDomain', 'PauseAfterReset', 'PCSystemType', 'PCSystemTypeEx', 'PowerManagementCapabilities', 'PowerManagementSupported', 'PowerOnPasswordStatus', 'PowerState', 'PowerSupplyState', 'PrimaryOwnerContact', 'PrimaryOwnerName', 'ResetCapability', 'ResetCount', 'ResetLimit', 'Roles', 'Status', 'SupportContactDescription', 'SystemFamily', 'SystemSKUNumber', 'SystemStartupDelay', 'SystemStartupOptions', 'SystemStartupSetting', 'SystemType', 'ThermalState', 'TotalPhysicalMemory', 'UserName', 'WakeUpType', 'Workgroup']
full_ram_information = []

# Get CPU information
cpu_info = cpuinfo.get_cpu_info()
cpu_percent = psutil.cpu_percent(interval=1)

# Get memory information
memory_info = psutil.virtual_memory()
ram_information = subprocess.check_output(['wmic', 'COMPUTERSYSTEM', 'get']).decode()
ram_AdminPasswordStatus = subprocess.check_output(['wmic', 'COMPUTERSYSTEM', 'get', 'AdminPasswordStatus']).decode()

for var in ram_vars:
    full_ram_information.append(subprocess.check_output(['wmic', 'COMPUTERSYSTEM', 'get', var]).decode())

for i in range(len(full_ram_information)):
    full_ram_information[i] = full_ram_information[i].split('\n')[1].strip()

for i in range(len(full_ram_information)):
    print(f"{ram_vars[i]}: {full_ram_information[i]}")

# ram_AdminPasswordStatus = full_ram_information.split('\n')[1].strip()
# ram_AutomaticManagedPagefile = full_ram_information.split('\n')[2].strip()
# ram_AutomaticResetBootOption = full_ram_information.split('\n')[3].strip()
# #ram_AutomaticResetCapability = full_ram_information.split('\n')[4].strip()
# ram_BootOptionOnLimit = full_ram_information.split('\n')[5].strip()
# ram_BootOptionOnWatchDog = full_ram_information.split('\n')[6].strip()
# ram_BootROMSupported = full_ram_information.split('\n')[7].strip()
# ram_BootStatus = full_ram_information.split('\n')[8].strip()
# ram_BootupState = full_ram_information.split('\n')[9].strip()
# ram_Caption = full_ram_information.split('\n')[10].strip()
# ram_ChassisBootupState = full_ram_information.split('\n')[11].strip()
# ram_ChassisSKUNumber = full_ram_information.split('\n')[12].strip()
# ram_CreationClassName = full_ram_information.split('\n')[13].strip()
# ram_CurrentTimeZone = full_ram_information.split('\n')[14].strip()
# ram_DaylightInEffect = full_ram_information.split('\n')[15].strip()
# ram_Description = full_ram_information.split('\n')[16].strip()
# ram_DNSHostName = full_ram_information.split('\n')[17].strip()
# ram_Domain = full_ram_information.split('\n')[18].strip()   
# ram_DomainRole = full_ram_information.split('\n')[19].strip()
# ram_EnableDaylightSavingsTime = full_ram_information.split('\n')[20].strip()
# ram_FrontPanelResetStatus = full_ram_information.split('\n')[21].strip()
# ram_HypervisorPresent = full_ram_information.split('\n')[22].strip()
# ram_InfraredSupported = full_ram_information.split('\n')[23].strip()
# ram_InitialLoadInfo = full_ram_information.split('\n')[24].strip()
# ram_InstallDate = full_ram_information.split('\n')[25].strip()
# ram_KeyboardPasswordStatus = full_ram_information.split('\n')[26].strip()
# ram_LastLoadInfo = full_ram_information.split('\n')[27].strip()
# ram_Manufacturer = full_ram_information.split('\n')[28].strip()
# ram_Model = full_ram_information.split('\n')[29].strip()
# ram_Name = full_ram_information.split('\n')[30].strip()
# ram_NameFormat = full_ram_information.split('\n')[31].strip()
# ram_NetworkServerModeEnabled = full_ram_information.split('\n')[32].strip()
# ram_NumberOfLogicalProcessors = full_ram_information.split('\n')[33].strip()
# ram_NumberOfProcessors = full_ram_information.split('\n')[34].strip()
# ram_OEMLogoBitmap = full_ram_information.split('\n')[35].strip()
# ram_OEMStringArray = full_ram_information.split('\n')[36].strip()
# ram_PartOfDomain = full_ram_information.split('\n')[37].strip()
# ram_PauseAfterReset = full_ram_information.split('\n')[38].strip()
# ram_PCSystemType = full_ram_information.split('\n')[39].strip()
# ram_PCSystemTypeEx = full_ram_information.split('\n')[40].strip()
# ram_PowerManagementCapabilities = full_ram_information.split('\n')[41].strip()
# ram_PowerManagementSupported = full_ram_information.split('\n')[42].strip()
# ram_PowerOnPasswordStatus = full_ram_information.split('\n')[43].strip()
# ram_PowerState = full_ram_information.split('\n')[44].strip()
# ram_PowerSupplyState = full_ram_information.split('\n')[45].strip()
# ram_PrimaryOwnerContact = full_ram_information.split('\n')[46].strip()
# ram_PrimaryOwnerName = full_ram_information.split('\n')[47].strip()
# ram_ResetCapability = full_ram_information.split('\n')[48].strip()
# ram_ResetCount = full_ram_information.split('\n')[49].strip()
# ram_ResetLimit = full_ram_information.split('\n')[50].strip()
# ram_Roles = full_ram_information.split('\n')[51].strip()
# ram_Status = full_ram_information.split('\n')[52].strip()
# ram_SupportContactDescription = full_ram_information.split('\n')[53].strip()
# ram_SystemFamily = full_ram_information.split('\n')[54].strip()
# ram_SystemSKUNumber = full_ram_information.split('\n')[55].strip()
# ram_SystemStartupDelay = full_ram_information.split('\n')[56].strip()
# ram_SystemStartupOptions = full_ram_information.split('\n')[57].strip()
# ram_SystemStartupSetting = full_ram_information.split('\n')[58].strip()
# ram_SystemType = full_ram_information.split('\n')[59].strip()
# ram_ThermalState = full_ram_information.split('\n')[60].strip()
# ram_TotalPhysicalMemory = full_ram_information.split('\n')[61].strip()
# ram_UserName = full_ram_information.split('\n')[62].strip()
# ram_WakeUpType = full_ram_information.split('\n')[63].strip()
# ram_Workgroup = full_ram_information.split('\n')[64].strip()

#ram_info = subprocess.check_output(['wmic', 'MEMORYCHIP', 'get', 'BankLabel', 'DeviceLocator', 'Capacity', 'Speed']).decode()

# Get disk information
disk_usage = psutil.disk_usage('/')
#disk_info = subprocess.check_output(['wmic', 'diskdrive', 'get', 'model', 'size']).decode()

# Get network information
network_info = psutil.net_io_counters()

# Get Motherboard information
#motherboard_info = subprocess.check_output(['wmic', 'baseboard', 'get', 'product', 'Manufacturer', 'version', 'serialnumber']).decode()

print("System Information: ")
print("=====================================")
print("cpu_info: ")
print(f"CPU Info: {cpu_info}")
print(f"CPU Usage: {cpu_percent}%")

print()
print("memory_info: ")
print(f"Memory Info: {memory_info}")
# print(f"RAM Info: {full_ram_information}")
# print(f"RAM AdminPasswordStatus: {ram_AdminPasswordStatus}")

# print(f"RAM AutomaticManagedPagefile: {ram_AutomaticManagedPagefile}")
# print(f"RAM AutomaticResetBootOption: {ram_AutomaticResetBootOption}")

# #print(f"RAM AutomaticResetCapability: {ram_AutomaticResetCapability}")
# print(f"RAM BootOptionOnLimit: {ram_BootOptionOnLimit}")
# print(f"RAM BootOptionOnWatchDog: {ram_BootOptionOnWatchDog}")
# print(f"RAM BootROMSupported: {ram_BootROMSupported}")
# print(f"RAM BootStatus: {ram_BootStatus}")
# print(f"RAM BootupState: {ram_BootupState}")
# print(f"RAM Caption: {ram_Caption}")
# print(f"RAM ChassisBootupState: {ram_ChassisBootupState}")
# print(f"RAM ChassisSKUNumber: {ram_ChassisSKUNumber}")
# print(f"RAM CreationClassName: {ram_CreationClassName}")
# print(f"RAM CurrentTimeZone: {ram_CurrentTimeZone}")
# print(f"RAM DaylightInEffect: {ram_DaylightInEffect}")
# print(f"RAM Description: {ram_Description}")
# print(f"RAM DNSHostName: {ram_DNSHostName}")
# print(f"RAM Domain: {ram_Domain}")
# print(f"RAM DomainRole: {ram_DomainRole}")
# print(f"RAM EnableDaylightSavingsTime: {ram_EnableDaylightSavingsTime}")
# print(f"RAM FrontPanelResetStatus: {ram_FrontPanelResetStatus}")
# print(f"RAM HypervisorPresent: {ram_HypervisorPresent}")
# print(f"RAM InfraredSupported: {ram_InfraredSupported}")
# print(f"RAM InitialLoadInfo: {ram_InitialLoadInfo}")
# print(f"RAM InstallDate: {ram_InstallDate}")
# print(f"RAM KeyboardPasswordStatus: {ram_KeyboardPasswordStatus}")
# print(f"RAM LastLoadInfo: {ram_LastLoadInfo}")
# print(f"RAM Manufacturer: {ram_Manufacturer}")
# print(f"RAM Model: {ram_Model}")
# print(f"RAM Name: {ram_Name}")
# print(f"RAM NameFormat: {ram_NameFormat}")
# print(f"RAM NetworkServerModeEnabled: {ram_NetworkServerModeEnabled}")
# print(f"RAM NumberOfLogicalProcessors: {ram_NumberOfLogicalProcessors}")
# print(f"RAM NumberOfProcessors: {ram_NumberOfProcessors}")
# print(f"RAM OEMLogoBitmap: {ram_OEMLogoBitmap}")
# print(f"RAM OEMStringArray: {ram_OEMStringArray}")
# print(f"RAM PartOfDomain: {ram_PartOfDomain}")
# print(f"RAM PauseAfterReset: {ram_PauseAfterReset}")
# print(f"RAM PCSystemType: {ram_PCSystemType}")
# print(f"RAM PCSystemTypeEx: {ram_PCSystemTypeEx}")
# print(f"RAM PowerManagementCapabilities: {ram_PowerManagementCapabilities}")
# print(f"RAM PowerManagementSupported: {ram_PowerManagementSupported}")
# print(f"RAM PowerOnPasswordStatus: {ram_PowerOnPasswordStatus}")
# print(f"RAM PowerState: {ram_PowerState}")
# print(f"RAM PowerSupplyState: {ram_PowerSupplyState}")
# print(f"RAM PrimaryOwnerContact: {ram_PrimaryOwnerContact}")
# print(f"RAM PrimaryOwnerName: {ram_PrimaryOwnerName}")
# print(f"RAM ResetCapability: {ram_ResetCapability}")
# print(f"RAM ResetCount: {ram_ResetCount}")
# print(f"RAM ResetLimit: {ram_ResetLimit}")
# print(f"RAM Roles: {ram_Roles}")
# print(f"RAM Status: {ram_Status}")
# print(f"RAM SupportContactDescription: {ram_SupportContactDescription}")
# print(f"RAM SystemFamily: {ram_SystemFamily}")
# print(f"RAM SystemSKUNumber: {ram_SystemSKUNumber}")
# print(f"RAM SystemStartupDelay: {ram_SystemStartupDelay}")
# print(f"RAM SystemStartupOptions: {ram_SystemStartupOptions}")
# print(f"RAM SystemStartupSetting: {ram_SystemStartupSetting}")
# print(f"RAM SystemType: {ram_SystemType}")
# print(f"RAM ThermalState: {ram_ThermalState}")
# print(f"RAM TotalPhysicalMemory: {ram_TotalPhysicalMemory}")
# print(f"RAM UserName: {ram_UserName}")
# print(f"RAM WakeUpType: {ram_WakeUpType}")
# print(f"RAM Workgroup: {ram_Workgroup}")

print()
print("disk_usage: ")
print(f"Disk Info: {disk_usage}") 
#print(f"Disk Info: {disk_info}")

print()
print("network_info: ")
print(f"Network Info: {network_info}")

#print(f"Motherboard Info: {motherboard_info}")