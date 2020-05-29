with open('ospf.txt', 'r') as config_file:
    cof_f = config_file.readlines()
    print(cof_f)
    def parse_conf(items):
        dict_access = {}
        if 'interface' in items:
            set_access = str(items)
            print(set_access)
        elif 'access' and 'vlan' in items:
            set_vlans = str(items)
            print(set_vlans)

    for items in cof_f:
        parse_conf(items)
    