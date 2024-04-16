import eel
import json
import subprocess
import os

eel.init('web')

# Need to use threads for more effieceint use of resources

# Get system information
import psutil

# Get system information
@eel.expose
def get_system_info():
    system_info = {}
    system_info['platform'] = os.uname().sysname
    system_info['release'] = os.uname().release
    system_info['version'] = os.uname().version
    system_info['machine'] = os.uname().machine

    # Get RAM info
    ram_info = psutil.virtual_memory()
    system_info['total_ram'] = round(ram_info.total / (1024 ** 3),2)  # Convert bytes to GB
    system_info['used_ram'] = round(ram_info.used / (1024 ** 3),2)  # Convert bytes to GB
    system_info['ram_percentage'] = ram_info.percent

    return system_info


# Json file for settings/config data
def read_json():
    if not os.path.exists('config.json'):
        default_data = {
            "key1": "default_value1",
            "key2": "default_value2",
            # Add more default values as needed
        }
        with open('config.json', 'w') as file:
            json.dump(default_data, file)
    
    with open('config.json', 'r') as file:
        data = json.load(file)
    return data

def write_json(data):
    with open('config.json', 'w') as file:
        json.dump(data, file)

# Runs given command in shell and returns output
@eel.expose
def test_commd(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

# Spawn a new shell with given command
@eel.expose
def spawn_shell(command):
    subprocess.Popen(command, shell=True)

eel.start('index.html', size=(300, 200), mode='firefox')