import psutil
import cpuinfo
import subprocess
import hashlib
from web3 import Web3

class info:
    def __init__(self):
        
        self.part_of_system_var = ['cpu', 'COMPUTERSYSTEM', 'diskdrive', 'nic', 'baseboard']
        
        self.cpu_vars = ['DeviceID', 'L2CacheSize', 'L3CacheSize', 'Manufacturer', 'Name', 'NumberOfCores', 'NumberOfLogicalProcessors', 'ProcessorId', 'SocketDesignation', 'SystemName']
        self.full_cpu_information = []
        
        self.ram_vars = ['Manufacturer', 'Model', 'Name', 'NumberOfLogicalProcessors', 'NumberOfProcessors', 'SystemType', 'TotalPhysicalMemory']
        self.full_ram_information = []
        
        self.disk_vars = ['DeviceID', 'FirmwareRevision', 'Model', 'Name', 'PNPDeviceID', 'SerialNumber', 'Size', 'SystemName']
        self.full_disk_information = []
        
        self.network_vars = ['DeviceID', 'Name', 'PNPDeviceID', 'ProductName', 'ServiceName', 'SystemName']
        self.full_network_information = []
        
        self.motherboard_vars = ['Manufacturer', 'Name', 'Product', 'SerialNumber', 'Tag', 'Version']
        self.full_motherboard_information = []
        
        self.using_cpu_vars = ['L2CacheSize', 'ProcessorId']
        self.full_using_cpu_vars = []
        
        self.using_ram_vars = ['NumberOfLogicalProcessors', 'TotalPhysicalMemory']
        self.full_using_ram_vars = []
        
        self.using_disk_vars = ['SerialNumber', 'Size']
        self.full_using_disk_vars = []
        
        self.using_vars = ['L2CacheSize', 'ProcessorId', 'NumberOfLogicalProcessors', 'TotalPhysicalMemory', 'SerialNumber', 'Size']
        self.full_using_vars = []
        
    ############################################################################################################
    
    ### CPU Information ###

    def get_cpu_information(self):
        for var in self.cpu_vars:
            self.full_cpu_information.append(subprocess.check_output(['wmic', 'cpu', 'get', var]).decode())

    def parse_cpu_information(self):
        i = 0
        while i < len(self.full_cpu_information):
            info = self.full_cpu_information[i].split('\n')[1].strip()
            if info:
                self.full_cpu_information[i] = info
                i += 1
            else:
                del self.full_cpu_information[i]
                del self.cpu_vars[i]

    def print_full_cpu_information(self):
        for i in range(len(self.full_cpu_information)):
            print(f"{self.cpu_vars[i]}: {self.full_cpu_information[i]}")

    ############################################################################################################
    
    ### RAM Information ###
    
    def get_ram_information(self):
        for var in self.ram_vars:
            self.full_ram_information.append(subprocess.check_output(['wmic', 'COMPUTERSYSTEM', 'get', var]).decode())
    
    def parse_ram_information(self):
        i = 0
        while i < len(self.full_ram_information):
            info = self.full_ram_information[i].split('\n')[1].strip()
            if info:
                self.full_ram_information[i] = info
                i += 1
            else:
                del self.full_ram_information[i]
                del self.ram_vars[i]
    
    def print_full_ram_information(self):
        for i in range(len(self.full_ram_information)):
            print(f"{self.ram_vars[i]}: {self.full_ram_information[i]}")
            
    ############################################################################################################
    
    ### Disk Information ###

    def get_disk_information(self):
        for var in self.disk_vars:
            self.full_disk_information.append(subprocess.check_output(['wmic', 'diskdrive', 'get', var]).decode())
    
    def parse_disk_information(self):
        i = 0
        while i < len(self.full_disk_information):
            info = self.full_disk_information[i].split('\n')[1].strip()
            if info:
                self.full_disk_information[i] = info
                i += 1
            else:
                del self.full_disk_information[i]
                del self.disk_vars[i]
    
    def print_full_disk_information(self):
        for i in range(len(self.full_disk_information)):
            print(f"{self.disk_vars[i]}: {self.full_disk_information[i]}")

    ############################################################################################################
    
    ### Network Information ###
    
    def get_network_information(self):
        for var in self.network_vars:
            self.full_network_information.append(subprocess.check_output(['wmic', 'nic', 'get', var]).decode())
    
    def parse_network_information(self):
        i = 0
        while i < len(self.full_network_information):
            info = self.full_network_information[i].split('\n')[1].strip()
            if info:
                self.full_network_information[i] = info
                i += 1
            else:
                del self.full_network_information[i]
                del self.network_vars[i]
    
    def print_full_network_information(self):
        for i in range(len(self.full_network_information)):
            print(f"{self.network_vars[i]}: {self.full_network_information[i]}")
            
    ############################################################################################################
    
    ### Motherboard Information ###
    
    def get_motherboard_information(self):
        for var in self.motherboard_vars:
            self.full_motherboard_information.append(subprocess.check_output(['wmic', 'baseboard', 'get', var]).decode())
    
    def parse_motherboard_information(self):
        i = 0
        while i < len(self.full_motherboard_information):
            info = self.full_motherboard_information[i].split('\n')[1].strip()
            if info:
                self.full_motherboard_information[i] = info
                i += 1
            else:
                del self.full_motherboard_information[i]
                del self.motherboard_vars[i]
    
    def print_full_motherboard_information(self):
        for i in range(len(self.full_motherboard_information)):
            print(f"{self.motherboard_vars[i]}: {self.full_motherboard_information[i]}")
    
    ############################################################################################################
    
    ### Get All Information ###
    
    def get_all_information(self):
        self.get_cpu_information()
        self.get_ram_information()
        self.get_disk_information()
        self.get_network_information()
        self.get_motherboard_information()
    
    def parse_all_information(self):
        self.parse_cpu_information()
        self.parse_ram_information()
        self.parse_disk_information()
        self.parse_network_information()
        self.parse_motherboard_information()
    
    def print_all_information(self):
        
        print("System Information: ")
        print("=====================================")
        
        print("cpu_info: ")
        self.print_full_cpu_information()
        
        print()
        print("=====================================")

        print("memory_info: ")

        self.print_full_ram_information()
        
        print()
        print("=====================================")

        print("disk_usage: ")
        self.print_full_disk_information()
        
        print()
        print("=====================================")

        print("network_info: ")
        self.print_full_network_information()
        
        print()
        print("=====================================")

        print("motherboard_info: ")
        self.print_full_motherboard_information()
        print("=====================================")
    
    ############################################################################################################

    ### Using Information ###
    
    def get_using_vars(self):
        for var in self.using_cpu_vars:
            self.full_using_cpu_vars.append(subprocess.check_output(['wmic', 'cpu', 'get', var]).decode())
            self.full_using_vars.append(subprocess.check_output(['wmic', 'cpu', 'get', var]).decode())
        for var in self.using_ram_vars:
            self.full_using_ram_vars.append(subprocess.check_output(['wmic', 'COMPUTERSYSTEM', 'get', var]).decode())
            self.full_using_vars.append(subprocess.check_output(['wmic', 'COMPUTERSYSTEM', 'get', var]).decode())
        for var in self.using_disk_vars:
            self.full_using_disk_vars.append(subprocess.check_output(['wmic', 'diskdrive', 'get', var]).decode())
            self.full_using_vars.append(subprocess.check_output(['wmic', 'diskdrive', 'get', var]).decode())
    
    def parse_using_vars(self):
        i = 0
        while i < len(self.full_using_vars):
            info = self.full_using_vars[i].split('\n')[1].strip()
            if info:
                self.full_using_vars[i] = info
                i += 1
            else:
                del self.full_using_vars[i]
                del self.using_vars[i]
    
    def print_using_vars(self):
        for i in range(len(self.full_using_vars)):
            print(f"{self.using_vars[i]}: {self.full_using_vars[i]}")
            
    ############################################################################################################
    
    ### COMPUTE HASH ###
    def hash_string_gen(self):
        pass
    
    
    def hash_with_keccak(self):
        return Web3.solidity_keccak(['string'], ['1234']).hex()
    
    def hash_cpu_information(self):
        cpu_info_string = ' '.join(self.full_cpu_information)
        return self.hash_with_keccak(cpu_info_string)
    
    def compute_hash(self):
        pass
            