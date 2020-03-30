import fire

import tully.network as network


class NetworkCli:
    def __init__(self):
        self.ip = network.ip
        self.nics = network.nics


class Cli:
    def __init__(self):
        self.network = NetworkCli


def main():
    fire.Fire(Cli)
