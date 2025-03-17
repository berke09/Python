import scapy.all as scapy
from scapy_http import http

def listening_packets(interface):
    try:
        # Start sniffing the packets on the specified interface
        scapy.sniff(iface=interface, store=False, prn=analyzing_packets)
    except Exception as e:
        print(f"Error in listening_packets: {e}")

def analyzing_packets(packet):
    try:
        # Check if the packet has HTTPRequest layer
        if packet.haslayer(http.HTTPRequest):
            if packet.haslayer(scapy.Raw):
                print(packet[scapy.Raw].load)
    except AttributeError as e:
        print(f"AttributeError in analyzing_packets: {e}")
    except Exception as e:
        print(f"Error in analyzing_packets: {e}")

if __name__ == "__main__":
    try:
        listening_packets("eth0")
    except Exception as e:
        print(f"Error starting packet listener: {e}")
