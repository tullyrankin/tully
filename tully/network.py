import socket
import sys
import subprocess


def ip():
    """Get IP address from default network route."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def nics():
    """Information on installed network interface cards."""
    if sys.platform == 'linux':
        return subprocess.call('ifconfig 2> /dev/null || ip addr')
    elif sys.platform == 'darwin':
        return subprocess.call('ifconfig')
    elif sys.platform == 'win32':
        return subprocess.call('ipconfig')
