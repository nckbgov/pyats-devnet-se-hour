# New module! Now using genie!
from genie.testbed import load
import os

# Loading device information
# Take the testbed file in the same directory where the python file is executed.
testbed = load('{cwd}/testbed.yaml'.format(cwd=os.path.dirname(__file__)))

# Looping for all devices in the testbed
for device in testbed:

    print('')

    device.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

    # Step 0: Saying on which device we are currently connected
    print('-----------------------------------')
    print('-- Connected on device: {device} --'.format(device=device.alias))
    print('-----------------------------------')

    # Step 1: Listing interfaces and IP addresses
    show_interface = device.parse('show ip interface brief')

    for interface in show_interface['interface']:
        print('{interface} -- {ip}'.format(interface=interface, 
                                        ip=show_interface['interface'][interface]['ip_address']))   
    
    print('')