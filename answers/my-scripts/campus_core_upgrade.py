import json
from mycoolpackage.my_cool_package import upgrader


with open("devices.json") as f:
    devices = json.load(f)

for d in devices:
    upgrader.upgrade(d["name"], d["target"])
