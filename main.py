import argparse
from HostBlocker import HostBlocker

parser = argparse.ArgumentParser(
    description='Takes a blocklist of hosts and writes or deletes those from the hosts file.'
    )

parser.add_argument('-bl', '--blocklist', required=True, help='Filepath to list of hosts to block')
parser.add_argument('-e', '--enable', action='store_true', help='Enable block list. Requires blocklist.')
parser.add_argument('-d', '--disable', action='store_true', help='Disable block list')

args = parser.parse_args()

blocker = HostBlocker(args.blocklist)

if args.activate:
    blocker.enable()
elif args.disable:
    blocker.disable()