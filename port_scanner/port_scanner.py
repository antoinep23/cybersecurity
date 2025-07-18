import time
from scapy.all import sr1, IP, TCP


# Define common ports and their associated services
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    110: "POP3",
    143: "IMAP",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP Alternate",
    6379: "Redis",
    27017: "MongoDB",
    5432: "PostgreSQL"
}

# Function to perform a simple port scan
def simple_port_scan(target, ports, mode):
    open_ports = []

    # Iterate through the list of ports and send SYN packets
    for port in ports:
        # Create a SYN packet
        packet = IP(dst=target)/TCP(dport=port, flags="S")

        # Send the packet and wait for a response
        res = sr1(packet, timeout=1, verbose=0)

        # Check if the response is a SYN-ACK or RST-ACK
        if res and res.haslayer(TCP):

            if res.getlayer(TCP).flags == 0x12:  # SYN-ACK (port open)
                open_ports.append(port)
                sr1(IP(dst=target)/TCP(dport=port, flags="R"), timeout=1, verbose=0)  # send RST flag to close the connection

            elif res.getlayer(TCP).flags == 0x14:  # RST-ACK (port closed)
                pass

        print("Scanned port {}: {}".format(port, "Open" if port in open_ports else "Closed"))
        
        # Sleep to control the speed of the scan
        if mode == "slow":
            time.sleep(10)
        elif mode == "ultra-slow":
            time.sleep(60)

    return open_ports


# Function to detect services based on open ports
def detect_services(target, ports=common_ports.keys(), mode="normal"):
    results = {}
    open_ports = simple_port_scan(target, ports, mode)
    for port in open_ports:
        service = common_ports.get(port, "Unknown")
        results[port] = service

    print("Open ports on {}: {}".format(target, open_ports))
    return results


# Allow target to be specified via command line argument
if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    detect_services(target)
