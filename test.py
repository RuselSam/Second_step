mask = input('Введите маску: ')
mask = int(mask)
if mask >=24 and mask <=32 :
    print('выполнился первый')
    n = 3
    l = (6 + (mask - 30))
    four_oktet = (('1' * 8 + '.') * n) + ('1' * l) + ('0' * (32 - mask))
    print(four_oktet)
    four_oktet = four_oktet.split('.')
    print('.'.join(four_oktet))
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