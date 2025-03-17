import subprocess
import re
import argparse
import sys

# Function to parse user inputs using argparse (modern alternative to optparse)
def get_inputs():
    parser = argparse.ArgumentParser(description="Change MAC address of a network interface.")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="interface to change")
    parser.add_argument("-m", "--mac", dest="mac_address", required=True, help="new mac address")
    return parser.parse_args()

# Function to change MAC address
def change_mac_address(user_interface, user_mac_address):
    try:
        # Bring the interface down, change the MAC, then bring it back up
        subprocess.call(["ifconfig", user_interface, "down"])
        subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
        subprocess.call(["ifconfig", user_interface, "up"])
        print(f"MAC address of {user_interface} changed to {user_mac_address}")
    except subprocess.CalledProcessError as e:
        print(f"Error changing MAC address: {e}")
        sys.exit(1)

# Function to validate and extract the MAC address from ifconfig output
def control_new_mac(interface):
    try:
        ifconfig = subprocess.check_output(["ifconfig", interface]).decode()
        new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
        if new_mac:
            return new_mac.group(0)
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving MAC address: {e}")
        sys.exit(1)

# Main Program
if __name__ == "__main__":
    print("MAC Changer Started!")

    # Get user inputs
    user_inputs = get_inputs()

    # Check if the entered MAC address format is valid
    mac_regex = re.compile(r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$")
    if not mac_regex.match(user_inputs.mac_address):
        print("Invalid MAC address format! Please enter a valid MAC address.")
        sys.exit(1)

    # Change the MAC address
    change_mac_address(user_inputs.interface, user_inputs.mac_address)

    # Verify if the MAC address was successfully changed
    finalized_mac = control_new_mac(user_inputs.interface)

    if finalized_mac == user_inputs.mac_address:
        print("Success! The MAC address was changed successfully.")
    else:
        print("Error! The MAC address could not be changed.")
