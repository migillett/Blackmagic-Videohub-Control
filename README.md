# Blackmagic Videohub Control
This program allows you to schedule and fire salvos for the [Blackmagic Videohub SDI video routers](https://www.blackmagicdesign.com/products/smartvideohub). You can do this through the command line or importing the script into another program for use with other forms of automation. Some examples would be cron jobs, custom button boxes, or scripts that could monitor the output and check for black video. The world is you oyster, so have fun with this.

## Requirements
The scripts in this repository require Python3 to run properly. You can download [Python3 here](https://www.python.org/downloads/).

The `bmd_scheduler.py` requires the python library `schedule` to work properly. Install it using `pip3 install schedule`. There are some examples in the script, but you can see more on how the library works in [their documentation](https://pypi.org/project/schedule/).

## How to use
There are 2 Python scripts in this repository. The most important one is `bmd_router_control.py`. You can import this script into other python files or even run it from the terminal. Here are some examples:


### Run from the terminal
You can call the script from the terminal using a command like this:
```
python3 ./bmd_router_control.py -a 192.168.1.30 -d 9 -s 10
```
The flags designate the following:
```
-a = the ip address of your video router

-d = the destination you want to patch the source into

-s = the source or input you want to route
```
  
In other words, the command above would route source 10 to output 9. Keep in mind that these are the sources as they are labeled on the back of the device. The video routers actually start at 0, not 1. But this is taken into account within the script, so you don't have to do the math.
 

### Import into another script
If you'd rather import the `bmd_router_control.py` into another script, it's super easy to do. Here's an example:

```
from bmd_router_control import blackmagic_router_control

router = blackmagic_router_control('192.168.1.30')

router.route_inputs([(1,2), (2,3), (4,6)])
```

The most important thing to remember is that the route_inputs command requires a list of tuples. It's formatted as (destination, source). So the command above would route input 2 to destination 1, input 3 to destination 2, and input 6 to destination 4. It's a little weird, but it's how you'd do it using the GUI.


## Scheduling Commands
If you'd rather not make your own way of queueing up commands, feel free to use the included `bmd_scheduler.py`. This script is pretty easy to use, just make sure you have the library `schedule` installed. Here's how it works:

1. Define when you want the command to trigger using military time
2. Replace the `192.168.1.30` on line 12 with the IP address of your router
3. (optional) define your own sources and destinations for readibility and ease-of-use later
4. Create your own functions to call later. There are 2 examples in there now that you can edit for your needs
5. Schedule when you want the scripts to run. Again, if you want help on how to use schedule, visit [their documentation](https://pypi.org/project/schedule/). Right now, they're scheduled to run the salvo every day at the time you specify.


## Contributing
Please feel free to share any improvements you have! This is a fairly new repository, so recommendations or improvements are always appreciated.


## Sources
Much of this repository is based on the [VideoHub SDK](https://downloads.blackmagicdesign.com/Developer/Videohub/20210215-b13954/Blackmagic_Videohub_Developer_SDK_1.0.zip) documentation provided by Blackmagic Design. For more information, visit their [developer page](https://www.blackmagicdesign.com/developer/).
