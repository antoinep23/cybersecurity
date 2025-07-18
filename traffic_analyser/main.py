import time
from scapy.all import sniff


# Store captured packets in a list
captured_packets = []

# Callback function to process each captured packet
def packet_callback(packet):
    packet_info = {
        'timestamp': time.time(),
        'src': packet.src if hasattr(packet, 'src') else 'N/A',
        'dst': packet.dst if hasattr(packet, 'dst') else 'N/A',
        'protocol': packet.name if hasattr(packet, 'name') else 'Unknown',
        'length': len(packet),
        'summary': packet.summary()
    }
    captured_packets.append(packet_info)

# Sniff packets on interface
sniff(prn=packet_callback)

