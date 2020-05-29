london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
router = input('Введите  имя устройства: ')
param = input('Введите имя парметра: '+str(london_co[router].keys())+' ').lower()
print(london_co[router].get(param, 'Такого параметра нет!'))


ip = input('Введите ip: ')
ip = ip.split('/')
ip1 = ip[0].split('.')
ip1[3] = 0
mask = int(ip[1])
print('''Network:\n{0:<8} {1:<8} {2:<8} {3:<8} \n{0:08b} {1:08b} {2:08b} {3:08b}'''.format(int(ip1[0]), int(ip1[1]), int(ip1[2]), int(ip1[3])))

mask = int(mask)
if mask >=24 and mask <=32 :
    print('выполнился первый')
    n = 3
    l = (6 + (mask - 30))
    four_oktet = (('1' * 8 + '.') * n) + ('1' * l) + ('0' * (32 - mask))
    print(four_oktet)
elif mask >=16 and mask <=23 :
    print('выполнился второй')
    n = 2
    l = (4 + (mask - 20))
    three_oktet = (('1' * 8 + '.') * n) + (('1' * l) + ('0' * (8-l)))+'.'+('0'*8)
    print(three_oktet)
elif mask >=8 and mask <=15 :
    print('выполнился третий')
    n = 1
    l = (2 + (mask - 10))
    two_oktet = (('1' * 8 + '.') * n) + (('1' * l) + ('0' * (8-l)))+('.'+('0'*8))*2
    print(two_oktet)
elif mask >=0 and mask <=7 :
    print('выполнился четвертый')
    l = mask
    one_oktet = (('1' * l) + ('0' * (8-l)))+('.'+('0'*8))*3
    print(one_oktet)

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
for macs in mac:
   macs = macs.replace(':','.')
   mac_cisco.append(macs)
print(mac_cisco)




while True:
    try:
        ip_add = str(input('Введите ip-адрес: '))
        ip_add = ip_add.split('.')
        ip_add = list(ip_add)
        ip_add.insert(1, '.')
        ip_add.insert(3, '.')
        ip_add.insert(5, '.')
        while len(ip_add) == 7:
            for element in ip_add[1::2]:
                while element == '.':
                    break
                else:
                     print('!!!Разделитель должен быть точками!!!\n')
            for element1 in ip_add[::2]:
                while (int(element1) >=0 and int(element1) <= 255):
                    break
                else:
                    print('!!!ip-адрес должен состоять из цифр от 0 до 255!!!\n')
            break
        else:
            print('!!!Некорректные данные!!!\n')
        if (int(ip_add[0]) >=1 and int(ip_add[0]) <=223):
            print('unicast\n')
        elif (int(ip_add[0]) >= 223 and int(ip_add[0]) <=239):
            print('multicast\n')
        elif (int(ip_add[0]) == 255 and int(ip_add[2]) == 255 and int(ip_add[4]) == 255 and int(ip_add[6]) == 255):
            print('local broadcast\n')
        elif (int(ip_add[0]) == 0 and int(ip_add[2]) == 0 and int(ip_add[4]) == 0 and int(ip_add[6]) == 0):
            print('unassigned\n')
        else:
            print('unused\n')
    except ValueError:
        print('!!!Некорректные данные!!!\n')
    if input() == 'stop':
        break

