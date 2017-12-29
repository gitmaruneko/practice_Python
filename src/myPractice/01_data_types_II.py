def show_me_list():

    numbers = [1, 2, 3, 4, 5, 6, 7];
    print("numbers:", numbers)
    numbers.append(8)
    print("numbers:", numbers)
    print()

    print("numbers[0] :", numbers[0])
    print("numbers[-1] :", numbers[-1])
    print("numbers[1:6] :", numbers[0:-1])
    print("numbers[::-1] :", numbers[::-1])
    print()

    numbers.reverse()
    print("numbers:", numbers)
    print()

    numbers2 = numbers
    numbers2[0] = 200
    print('numbers:', numbers)
    print('numbers2:', numbers2)
    print()

    numbers3 = numbers.copy()
    numbers3[0] = 2000
    print('numbers:', numbers)
    print('numbers3:', numbers3)
    print()

    mixed_list = numbers.copy()
    mixed_list.append("x")
    print("mixed_list : ", mixed_list)

    print("list(range(3)):", list(range(3)))
    print("list(range(1, 3)):", list(range(1, 3)))
    print("list(range(1, 3+1)):", list(range(1, 3+1)))
    print("list(range(0, 10, 2)):", list(range(0, 10, 2)))

def show_me_dict():

    id_name_map = {
        'heidi.huang': 'Heidi Huang',
        'heidi.bot': 'Heidi Bot',
    }
    print('id_name_map : ', id_name_map)
    print('.keys : ', id_name_map.keys())
    print('.values : ', id_name_map.values())
    print('.items : ', id_name_map.items())
    print()

def show_me_tuple():

    print('single:', (1, ))
    xypair_item_map = {
        (10, 20): '$100'
    }
    print('xypair_item_map :', xypair_item_map)
    print()

    pair = (1, 2)
    a, b = pair
    print('pair:', pair)
    print('a:', a)
    print('b', b)
    print()
    numbers = [1, 2, 3, 4, 5, 6, 7];
    pair2 = list(pair)
    pair3 = numbers + pair2
    print(pair3)



if __name__ == '__main__':
    #show_me_list()
    #show_me_dict()
    show_me_tuple()