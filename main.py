#!/usr/bin/python3

import argparse
import subprocess

from exceptions import InterfaceNotFound

def get_stats(interface):

    check=subprocess.run(["ifconfig", interface], capture_output=True)
    if bool(check.stderr):
        raise InterfaceNotFound("Interface {} not found".format(interface))

    stats=subprocess.run(["ethtool", "-S", interface], capture_output=True)

def get_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interface", type=str,
                        help="Interface name")

    return parser.parse_args()

if __name__=="__main__":

    args = get_args()
    get_stats(args.interface)
