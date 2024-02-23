import subprocess
import optparse
import re

def get_intputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")
    return parse_object.parse_args()

def change_mac_address(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return  None

print("my mac changer started!")
(user_inputs,arguments) = get_intputs()
change_mac_address(user_inputs.interface,user_inputs.mac_address)
finalized_mac = control_new_mac(str(user_inputs.interface))

if finalized_mac == user_inputs.mac_address:
    print("Success!")
else:
    print("Error!")
