from typing import List

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


def nics() -> List[str]:
    """Information on installed network interface cards."""
    output = []

    if sys.platform == 'linux':
        try:
            # first we try ip addr command
            out = subprocess.Popen(["ip", "addr"],
                                   stdout=subprocess.PIPE)
            stdout, stderr = out.communicate()
            output = stdout.decode('utf-8').split("\n")
        except FileNotFoundError:
            # ip addr command failed so lets try ifconfig
            out = subprocess.Popen("ifconfig",
                                   stdout=subprocess.PIPE)
            stdout, stderr = out.communicate()
            output = stdout.decode('utf-8').split("\n")
    elif sys.platform == 'darwin':
        return subprocess.call('ifconfig')
    elif sys.platform == 'win32':
        return subprocess.call('ipconfig')

    return output


def host_ip(hostname: str) -> str:
    """Retrieves IP address from DNS for given hostname."""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return "No record found."
