import scapy.all as scapy
from scapy_http import http

def listening_packets(interface):
    scapy.sniff(iface=interface,store=False,prn=analyzing_packets)
def analyzing_packets(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

listening_packets("eth0")