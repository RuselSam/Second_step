access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]
access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

def config_interface (interf, vl,psecurity=None):
   print(f'interface  {interf}')
   for inf in access_mode_template:
        if 'vlan' in inf:
           print(inf + ' ' + str(vl))
           continue
        print(inf)
   if psecurity == 1:
       for values in port_security_template:
           print(values)

for g,t in access_config.items():
    config_interface(g,t,1)