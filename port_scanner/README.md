# SYN Port Scanner

A simple TCP port scanner that uses SYN packets for stealthy scanning.

## Features

- **SYN Scanning Technique**:
  - Sends SYN packet to target ports
  - Identifies open ports by SYN-ACK responses
  - Automatically closes connection with RST to minimize network impact
- **3 Scanning Modes**:
  - **Normal mode**: Fast scanning (default)
  - **Slow mode**: Adds delay between requests for more discreet scanning (10sec)
  - **Ultra slow mode**: Adds delay between requests for ultra discreet scanning (60sec)
- **Common Service Detection**: Automatically identifies well-known services
- **Lightweight**: Pure Python implementation using Scapy

## Usage

### 1. Installation

First install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Basic scanning

```python
from port_scanner import detect_services

# Scan target with default common ports
target = "example.com"  # Can use IP or domain
detect_services(target)
```

### 3. Custom ports and scan mode

```python
target = "192.168.1.100"
ports_to_scan = [22, 80, 443, 8080, 9000]  # leave as default for common ports
speed_mode = "slow"  # or "ultra-slow", leave as default for "normal" mode

# Available modes:
# - "normal" (default, no delay)
# - "slow" (10s between ports)
# - "ultra-slow" (60s between ports)

detect_services(
    target=target,
    ports=ports_to_scan,
    mode=speed_mode
)
```

### Can also be used via terminal

```bash
python3 port_scanner.py example.com
```

If the target isn't specified, then your local host 127.0.0.1 is scanned.

## Disclaimer

Use this tool only on networks you own or have permission to scan. Port scanning without authorization may violate laws or network policies.

---

github.com/antoinep23
