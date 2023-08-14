import telnetlib
from datetime import datetime
import argparse

# This program is an importable way to control the blackmagic cleanswitch 12x12 videohub
# Written by Michael Gillett, 2021

# Based on the Developer SDK provided by Blackmagic Design
# https://www.blackmagicdesign.com/developer/

# This is the base program, but this is best used when imported into another automation program
# You can also use this from the terminal too.
# for example:
# python3 ./bmd_router_control.py -a 192.168.1.30 -s 12 -d 1

parser = argparse.ArgumentParser(
    description='Set and Get Blackmagic VideoHub configurations.')
parser.add_argument('-d', '--destination', dest='destination',
                    type=int, nargs=1, help="Get cross point source for destination")
parser.add_argument('-s', '--source', dest='source', type=int, nargs=1,
                    help="Set cross point source for destination (defined by -d)")
parser.add_argument('-a', '--address', dest='address', type=str,
                    nargs=1, help="IP address or DNS name of the video router")
args = parser.parse_args()


def generate_timestamp() -> str:
    return str(datetime.now())


class blackmagic_router_control():
    def __init__(self, host, port: int = 9990, timeout_seconds: int = 5) -> None:
        self.timeout = timeout_seconds
        self.host = host
        self.port = port

    def init_connection(self) -> bool:
        # need to add a try and except error here for bad ip, port
        try:
            self.tn = telnetlib.Telnet(self.host, self.port, self.timeout)
            print(
                f'{generate_timestamp()} | Established connection with {self.host}:{self.port}')
            return True
        
        except Exception as e:
            print(f'{e}: Unable to connect to video router. Please reconfigure and try again.\n'))
            return False
                
    # routing_commands need to be a list of touples.
    # ie: [(destination, source), (destination, source)]
    def route_inputs(self, routing_commands: list = []) -> None:
        print(f'{generate_timestamp()} | Routing Inputs: {routing_commands}')
        cmd = 'video output routing:\n'
        for pair in routing_commands:
            cmd += f'{pair[0]-1} {pair[1]-1}\n'
        cmd += '\n'  # the router requires 2 blank lines at the end of every command
        self.execute(cmd)

    def route_single(self, destination: int, source: int) -> None:
        print(f'{generate_timestamp()} | Routing {source} to {destination}')
        cmd = f'video output routing:\n{destination-1} {source-1}\n\n'
        self.execute(cmd)

    def execute(self, command: str) -> bool:
        if self.init_connection():
            # execute command
            self.tn.read_until(b"END PRELUDE:")
            print(f'Executing command: {command}')
            self.tn.write((command).encode('ascii'))
            self.tn.read_until(b"ACK", self.timeout)

            print(
                f'{generate_timestamp()} | Switch command confirmed by router at {self.host}:{self.port}')

            # close connection
            self.tn.close()
            return True
        
        else:
            return False


if __name__ == '__main__':
    # try and pull the router address. if none defined, require input.
    try:
        addr = args.address[0]
    except TypeError:
        addr = str(input('\nInput router IP address: '))

        # try and pull the destination. if none defined, require input.
    try:
        dst = args.destination[0]
    except TypeError:
        dst = int(input('\nInput destination: '))

        # try and pull the source. if none defined, send false and continue.
    try:
        src = args.source[0]
    except TypeError:
        src = int(input('\nInput source: '))

    router = blackmagic_router_control(host=addr)
    router.route_single(destination=dst, source=src)

    # For testing connection issues
    # router = blackmagic_router_control(host='0.0.0.0')
    # router.route_single(destination=1, source=1)
