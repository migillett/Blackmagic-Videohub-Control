from time import sleep
import schedule
from bmd_router_control import blackmagic_router_control
from functions.display_time import *

# Change the show start and end times here. Use military time, so 1:00 pm = 13:00
city_hall_start = '18:29:50'
gc360_start = '15:59:50'
gc360_end = '16:30:00'

# Setup router command here (put your router's ip below)
router = blackmagic_router_control('192.168.1.30')

# SOURCES (for easier readability)
tricaster_pgm = 6
scala = 9
city_hall = 10
terrell_in = 11
centennial = 12

# DESTINATIONS (for easier readability)
headend = 1
monitor_rack = 8
monitor_record = 9
monitor_playback = 10
recorder = 11
terrell_send = 12


def gc360():
    router.route_inputs([
        (terrell_in, headend),
        (terrell_in, monitor_rack),
        (terrell_in, terrell_send)])


def default():
    router.route_inputs([
        (scala, headend),
        (scala, monitor_rack),
        (scala, terrell_send)])


schedule.every().day.at(gc360_start).do(gc360)
schedule.every().day.at(gc360_end).do(default)


if __name__ == '__main__':
    print('=======================\n  Program initialized.\n=======================\n')
    while True:
        try:
            t = schedule.idle_seconds()
            print('Time until next switch command:', display_time(t))
        except TypeError:
            print('\nNo switch scheduled. Exiting.')
            break
        schedule.run_pending()
        sleep(1)
