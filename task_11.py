with open('show_cdp_neighbor.txt', 'r') as show_c:
    show_c = list(show_c)

def parse_cdp_neighbors(command_output):
    device = []
    local_interface = []
    port_id = []
    cdp_neighbors_dict = {}
    for items in command_output:
        if ('R' or 'SW') in items:
            items = items.split()
            device.append(items[0])
            local_interface.append('Fa'+items[2])
            port_id.append('Fa'+items[-1])
            continue
        for dev in device:
            if len(str(dev)) > 2:
                x = device.index(dev)
                dev = dev[0:2]
                device[x] = dev
    local_interface = list(filter(lambda inter: "/" in inter, local_interface))
    port_id = list(filter(lambda port: "/" in port, port_id))
    for elements in range(len(port_id)):
        cdp_neighbors_dict.update({(device[0], local_interface[elements]): (device[elements], port_id[elements])})
    return cdp_neighbors_dict

parse_cdp_neighbors(show_c)