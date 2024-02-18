import json

with open('/vs/PP2/tsis4/sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 88)
print("{:<60}{:<20}{:<10}{:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in data["interface_status"]:
    dn = interface["DN"]
    description = interface["Description"]
    speed = interface["Speed"]
    mtu = interface["MTU"]
    print("{:<60}{:<20}{:<10}{:<6}".format(dn, description, speed, mtu))
