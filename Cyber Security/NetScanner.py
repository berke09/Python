import scapy.all as scapy
import optparse


# Function to handle user input
def get_user_inputs():
    try:
        parse_object = optparse.OptionParser()
        parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="IP address to scan")
        (user_inputs, arguments) = parse_object.parse_args()

        # Validate input
        if not user_inputs.ip_address:
            print("Please enter an IP address...")
            exit(1)  # Exit if no IP address is provided

        return user_inputs
    except Exception as e:
        print(f"Error in get_user_inputs: {e}")
        exit(1)


# Function to perform a network scan
def my_net_scanner(ip):
    try:
        # Create ARP request packet
        arp_request_packet = scapy.ARP(pdst=ip)
        # Create broadcast packet
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        # Combine the ARP request with the broadcast
        combined_packet = broadcast_packet / arp_request_packet

        # Send the packet and capture the responses
        answered_list, unanswered_list = scapy.srp(combined_packet, timeout=1, verbose=False)

        # Display results
        print(f"IP Address\t\tMAC Address")
        print("-------------------------------------------")
        for element in answered_list:
            print(f"{element[1].psrc}\t\t{element[1].hwsrc}")

    except scapy.error.Scapy_Exception as e:
        print(f"Scapy error occurred: {e}")
    except Exception as e:
        print(f"Error in my_net_scanner: {e}")


# Main function to run the script
def main():
    try:
        user_ip_address = get_user_inputs()  # Get user input
        my_net_scanner(user_ip_address.ip_address)  # Perform network scan
    except Exception as e:
        print(f"Error in main function: {e}")
        exit(1)


if __name__ == "__main__":
    try:
        main()  # Run the main function
    except Exception as e:
        print(f"An error occurred while running the script: {e}")
