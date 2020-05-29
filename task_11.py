with open('show_cdp_neighbor.txt', 'r') as show_c:
    show_c = list(show_c)

def parse_cdp_neighbors(command_output):
    device = []
    interface = []
    for items in command_output:
        if 'R' in items:
            items = items.split()
        else:
            continue
        for devices in items:
            if 'R' in devices and len(str(devices)) > 1:
                device.append(devices)
            elif '/' in devices:
                interface.append('Fa'+devices)
                continue
        for dev in device:
            if len(str(dev)) > 2:
                x = device.index(dev)
                dev = dev[0:2]
                device[x] = dev
                continue
    cdp_neighbors_dict = {(device[0], interface[1]) : (device[1], interface[0]), (device[0], interface[2]): (device[2], interface[3])}
    return cdp_neighbors_dict

parse_cdp_neighbors(show_c)