# DABABI

APPLICATION FOR BCHW VERIFICATION
- [DABABI](#dababi)
- [Table of Contents](#table-of-contents)
- [About the application](#about-the-application)
- [CPU variables list](#cpu-variables-list)
- [Memory variables list](#memory-variables-list)
- [Disk variables list](#disk-variables-list)
- [Network variables list](#network-variables-list)
- [Motherboard variables list](#motherboard-variables-list)
- [Hash implementation](#hash-implementation)
- [Flask server](#flask-server)

# Table of Contents

# About the application

![image](py_src/static/DABABI_MADE_TO_SIZE.png)

This part of the application will get the specific system identifiers including but not limited to:
cpu, memory, disk, network, and other system information. 
The application will then send the information to the server for verification. 
The server will then verify the information and send back a response to the client. 
The client will then display the response to the user.

------------------------------------------------------

# CPU variables list

- DeviceID: This is a unique identifier for the device.
- L2CacheSize: This indicates the size of the level 2 cache and won't change unless the hardware is physically modified.
- L3CacheSize: This indicates the size of the level 3 cache and won't change unless the hardware is physically modified.
- Manufacturer: This indicates the manufacturer of the processor and won't change.
- Name: This indicates the name of the processor and won't change.
- NumberOfCores: This indicates the number of cores in the processor and won't change unless the hardware is physically modified.
- NumberOfLogicalProcessors: This indicates the number of logical processors and won't change unless the hardware is physically modified.
- ProcessorId: This is a unique identifier for the processor.
- SocketDesignation: This indicates the socket or slot where the processor is installed and won't change unless the hardware is physically modified.
- SystemName: This is the name of the computer system and won't change unless it's manually changed by the user.

```python
full_cpu_vars = ['AddressWidth', 'Architecture', 'AssetTag', 'Availability', 'Caption', 'Characteristics', 'ConfigManagerErrorCode', 'ConfigManagerUserConfig', 'CpuStatus', 'CreationClassName', 'CurrentClockSpeed', 'CurrentVoltage', 'DataWidth', 'Description', 'DeviceID', 'ErrorCleared', 'ErrorDescription', 'ExtClock', 'Family', 'InstallDate', 'L2CacheSize', 'L2CacheSpeed', 'L3CacheSize', 'L3CacheSpeed', 'LastErrorCode', 'Level', 'LoadPercentage', 'Manufacturer', 'MaxClockSpeed', 'Name', 'NumberOfCores', 'NumberOfEnabledCore', 'NumberOfLogicalProcessors', 'OtherFamilyDescription', 'PartNumber', 'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'ProcessorId', 'ProcessorType', 'Revision', 'Role', 'SecondLevelAddressTranslationExtensions', 'SerialNumber', 'SocketDesignation', 'Status', 'StatusInfo', 'Stepping', 'SystemCreationClassName', 'SystemName', 'ThreadCount', 'UniqueId', 'UpgradeMethod', 'Version', 'VirtualizationFirmwareEnabled', 'VMMonitorModeExtensions', 'VoltageCaps']

cpu_vars = ['DeviceID', 'L2CacheSize', 'L3CacheSize', 'Manufacturer', 'Name', 'NumberOfCores', 'NumberOfLogicalProcessors', 'ProcessorId', 'SocketDesignation', 'SystemName']

full_cpu_information = []
```

# Memory variables list

- Manufacturer: This indicates the manufacturer of the system and won't change.
- Model: This indicates the model of the system and won't change.
- Name: This is the name of the computer system and won't change unless it's manually changed by the user.
- NumberOfLogicalProcessors: This indicates the number of logical processors and won't change unless the hardware is physically modified.
- NumberOfProcessors: This indicates the number of processors and won't change unless the hardware is physically modified.
- SystemType: This indicates the type of system and won't change.
- TotalPhysicalMemory: This indicates the total physical memory and won't change unless the hardware is physically modified.

```python
full_ram_vars = ['AdminPasswordStatus', 'AutomaticManagedPagefile', 'AutomaticResetBootOption', 'AutomaticResetCapability', 'BootOptionOnLimit', 'BootOptionOnWatchDog', 'BootROMSupported', 'BootStatus', 'BootupState', 'Caption', 'ChassisBootupState', 'ChassisSKUNumber', 'CreationClassName', 'CurrentTimeZone', 'DaylightInEffect', 'Description', 'DNSHostName', 'Domain', 'DomainRole', 'EnableDaylightSavingsTime', 'FrontPanelResetStatus', 'HypervisorPresent', 'InfraredSupported', 'InitialLoadInfo', 'InstallDate', 'KeyboardPasswordStatus', 'LastLoadInfo', 'Manufacturer', 'Model', 'Name', 'NameFormat', 'NetworkServerModeEnabled', 'NumberOfLogicalProcessors', 'NumberOfProcessors', 'OEMLogoBitmap', 'OEMStringArray', 'PartOfDomain', 'PauseAfterReset', 'PCSystemType', 'PCSystemTypeEx', 'PowerManagementCapabilities', 'PowerManagementSupported', 'PowerOnPasswordStatus', 'PowerState', 'PowerSupplyState', 'PrimaryOwnerContact', 'PrimaryOwnerName', 'ResetCapability', 'ResetCount', 'ResetLimit', 'Roles', 'Status', 'SupportContactDescription', 'SystemFamily', 'SystemSKUNumber', 'SystemStartupDelay', 'SystemStartupOptions', 'SystemStartupSetting', 'SystemType', 'ThermalState', 'TotalPhysicalMemory', 'UserName', 'WakeUpType', 'Workgroup']

ram_vars = ['Manufacturer', 'Model', 'Name', 'NumberOfLogicalProcessors', 'NumberOfProcessors', 'SystemType', 'TotalPhysicalMemory']

full_ram_information = []
```

# Disk variables list

- DeviceID: This is a unique identifier for the disk drive.
- FirmwareRevision: This indicates the firmware revision of the disk drive and won't change unless the firmware is updated.
- Model: This indicates the model of the disk drive and won't change.
- Name: This is the name of the disk drive and won't change unless it's manually changed by the user.
- PNPDeviceID: This is a unique identifier for the disk drive.
- SerialNumber: This is a unique identifier for the disk drive.
- Size: This indicates the size of the disk drive and won't change unless the hardware is physically modified.
- SystemName: This is the name of the computer system and won't change unless it's manually changed by the user.

```python
full_disk_vars = ['Availability', 'BytesPerSector', 'Capabilities', 'CapabilityDescriptions', 'Caption', 'CompressionMethod', 'ConfigManagerErrorCode', 'ConfigManagerUserConfig', 'CreationClassName', 'DefaultBlockSize', 'Description', 'DeviceID', 'ErrorCleared', 'ErrorDescription', 'ErrorMethodology', 'FirmwareRevision', 'Index', 'InstallDate', 'InterfaceType', 'LastErrorCode', 'Manufacturer', 'MaxBlockSize', 'MaxMediaSize', 'MediaLoaded', 'MediaType', 'MinBlockSize', 'Model', 'Name', 'NeedsCleaning', 'NumberOfMediaSupported', 'Partitions', 'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'SCSIBus', 'SCSILogicalUnit', 'SCSIPort', 'SCSITargetId', 'SectorsPerTrack', 'SerialNumber', 'Signature', 'Size', 'Status', 'StatusInfo', 'SystemCreationClassName', 'SystemName', 'TotalCylinders', 'TotalHeads', 'TotalSectors', 'TotalTracks', 'TracksPerCylinder']

disk_vars = ['DeviceID', 'FirmwareRevision', 'Model', 'Name', 'PNPDeviceID', 'SerialNumber', 'Size', 'SystemName']

full_disk_information = []
```

# Network variables list

- DeviceID: This is a unique identifier for the network adapter.
- Name: This is the name of the network adapter and won't change unless it's manually changed by the user.
- PNPDeviceID: This is a unique identifier for the network adapter.
- ProductName: This indicates the product name of the network adapter and won't change.
- ServiceName: This indicates the service name of the network adapter and won't change.
- SystemName: This is the name of the computer system and won't change unless it's manually changed by the user.

```python
full_network_vars = ['AdapterType', 'AdapterTypeId', 'AutoSense', 'Availability', 'Caption', 'ConfigManagerErrorCode', 'ConfigManagerUserConfig', 'CreationClassName', 'Description', 'DeviceID', 'ErrorCleared', 'ErrorDescription', 'GUID', 'Index', 'InstallDate', 'Installed', 'InterfaceIndex', 'LastErrorCode', 'MACAddress', 'Manufacturer', 'MaxNumberControlled', 'MaxSpeed', 'Name', 'NetConnectionID', 'NetConnectionStatus', 'NetEnabled', 'NetworkAddresses', 'PermanentAddress', 'PhysicalAdapter', 'PNPDeviceID', 'PowerManagementCapabilities', 'PowerManagementSupported', 'ProductName', 'ServiceName', 'Speed', 'Status', 'StatusInfo', 'SystemCreationClassName', 'SystemName', 'TimeOfLastReset']

network_vars = ['DeviceID', 'Name', 'PNPDeviceID', 'ProductName', 'ServiceName', 'SystemName']

full_network_information = []
```

# Motherboard variables list

- Manufacturer: This indicates the manufacturer of the motherboard and won't change.
- Name: This is the name of the motherboard and won't change unless it's manually changed by the user.
- Product: This indicates the product name of the motherboard and won't change.
- SerialNumber: This is a unique identifier for the motherboard.
- Tag: This is a tag for the motherboard and won't change unless it's manually changed by the user.
- Version: This indicates the version of the motherboard and won't change unless the hardware is physically modified.

```python
full_motherboard_vars = ['Caption', 'ConfigOptions', 'CreationClassName', 'Depth', 'Description', 'Height', 'HostingBoard', 'HotSwappable', 'InstallDate', 'Manufacturer', 'Model', 'Name', 'OtherIdentifyingInfo', 'PartNumber', 'PoweredOn', 'Product', 'Removable', 'Replaceable', 'RequirementsDescription', 'RequiresDaughterBoard', 'SerialNumber', 'SKU', 'SlotLayout', 'SpecialRequirements', 'Status', 'Tag', 'Version', 'Weight', 'Width']

motherboard_vars = ['Manufacturer', 'Name', 'Product', 'SerialNumber', 'Tag', 'Version']

full_motherboard_information = []
```

# Hash implementation

The hash implementation is done using the SHA-256 algorithm.
The hash is generated by concatenating the system information and then hashing it using the SHA-256 algorithm.

```python
def generate_hash(system_information):
    hash_object = hashlib.sha256()
    hash_object.update(system_information.encode())
    return hash_object.hexdigest()
```

For security, the hash is then sent to the server for verification. The server will then verify the hash and send back a response to the client. The users password is never sent to the server and is only used to generate the hash.

# Flask server

The server is implemented using Flask. The server will receive the system information and hash from the client, verify the hash, and send back a response to the client.

first we need to install flask using the following command:

```bash
pip install flask
```

The server code is as follows:

```python
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    system_information = data['system_information']
    hash_value = data['hash']
    generated_hash = generate_hash(system_information)
    if hash_value == generated_hash:
        return jsonify({'response': 'Verification successful'})
    else:
        return jsonify({'response': 'Verification failed'})
```

For source code and images, a static and templates folder is created. The static folder contains the images and the templates folder contains the HTML file.


