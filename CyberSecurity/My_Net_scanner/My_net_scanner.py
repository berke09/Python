import scapy.all as scapy
import optparse

# ARP request
# broadcast
# response

def get_user_inputs():
    parse_object= optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest = "ip_address",help = "getting ip address")
    (user_inputs,arguments) = parse_object.parse_args()
    if not user_inputs.ip_address:
        print("please enter an ip address...")
    return user_inputs

def my_net_scaner(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    scapy.ls(scapy.Ether())
    combined_packet =broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    #print(list(answered_list))
    answered_list.summary()

user_ip_address = get_user_inputs()
my_net_scaner(user_ip_address.ip_address)

