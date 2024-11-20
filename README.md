# Blackmagic Videohub Control
This program allows you to schedule and fire salvos for the [Blackmagic Videohub SDI video routers](https://www.blackmagicdesign.com/products/smartvideohub). You can do this through the command line or importing the script into another program for use with other forms of automation. Some examples would be cron jobs, custom button boxes, or scripts that could monitor the output and check for black video. The world is you oyster, so have fun with this.

## Installing
Installation is pretty painless. Just run the following command:
```bash
pip3 install git+https://github.com/migillett/Blackmagic-Videohub-Control@v1.1.0
```

To import this into your other Python3 programs, just do this:
```python
from blackmagic_videohub_control import BlackmagicRouterControl, RouteCommand

router = BlackmagicRouterControl('192.168.2.2')
router.route_single(source=1, destination=1)
```

## Requirements
The scripts in this repository require Python3 to run properly. You can download [Python3 here](https://www.python.org/downloads/). The software does utilize `telnetlib` to talk to the Videohub, but that's built-in to Python3.


### Run from the terminal
You can call the script from the terminal using a command like this:
```
python3 ./blackmagic_videohub_control/main.py -a 192.168.1.30 -d 9 -s 10
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
from blackmagic_router_control import BlackmagicRouterControl, RouteCommand

router = BlackmagicRouterControl('192.168.1.30')

cmds = [
    RouteCommand(src=1, dst=2),
    RouteCommand(src=2, dst=3),
    RouteCommand(src=4, dst=6)
]

router.route_inputs(cmds)
```

If that's not quite your cup of tea, you can instead use the `route_single` command. All you have to do there is pass through the source and destination as arguments and it'll execute a command for you. There is no salvo support for pre-defined configs, but it is a bit easier for one-off setups. For example:

`router.route_single(destination=4, source=3)`


## Contributing
Please feel free to share any improvements you have! Recommendations or improvements are always appreciated.


## Sources
Much of this repository is based on the [VideoHub SDK](https://downloads.blackmagicdesign.com/Developer/Videohub/20210215-b13954/Blackmagic_Videohub_Developer_SDK_1.0.zip) documentation provided by Blackmagic Design. For more information, visit their [developer page](https://www.blackmagicdesign.com/developer/).
