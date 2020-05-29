trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def generate_trunk_config(interf, *vlans):
    ##генератор транковой конфигурации
    st = interf
    for template in trunk_mode_template:
        if 'allowed' in template:
            rt = (template + ' '+str(*vlans)+' ')
            continue
        vt = template
    result = {st:rt+vt}
    return print(result)

for interfaces, vlan in trunk_config.items():
    generate_trunk_config(interfaces, vlan)