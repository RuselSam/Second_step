with open('ospf.txt', 'r') as ospf_file:
    ospf_list = ospf_file.read().split()
    ospf_list[0] = 'OSPF'
    ospf_list.pop(3)
    d1 = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
    new_dict = dict.fromkeys(d1)
    list4 = list(new_dict)
    x = 0
    y = 0
    while(x < len(new_dict)):
        if x <= (len(new_dict)-1) and y <= (len(ospf_list)-1):
            m = ospf_list[y]
            m = str(m)
            new_dict[list4[x]] = m
            x += 1
            y += 1
        else:
            break
    for key, value in new_dict.items():
        print(key+' : '+value)