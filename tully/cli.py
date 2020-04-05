import fire

from tully import __version__ as version
import tully.network as network

VERSION_FANCY = f"""\
 _____     _ _
|_   _|  _| | |_  _
  | || || | | | || |
  |_| \_,_|_|_|\_, |
               |__/
Version: {version}"""


class NetworkCli:
    def __init__(self):
        self.host = network.host_ip
        self.ip = network.ip
        self.nics = network.nics


class Cli:
    def __init__(self):
        self.network = NetworkCli
        self.version = lambda: VERSION_FANCY


def main():
    fire.Fire(Cli)
