import random
my_list, rand_list = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_tup = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
p1_choice, p2_choice, count, p, p1, p1_list, p2_list = '', '', 0, True, True, [], []


def show():
    global p1_choice
    global p2_choice
    global p
    print('--------------')
    print('|', my_list[1], '|', my_list[2], '|', my_list[3], '|')
    print('-------------')
    print('|', my_list[4], '|', my_list[5], '|', my_list[6], '|')
    print('-------------')
    print('|', my_list[7], '|', my_list[8], '|', my_list[9], '|')
    print('--------------')
    while p:
        p1_choice = input("Player Select Your Choice 'X' or 'O'\n")
        if p1_choice in ['X', 'O']:
            if p1_choice == 'X':
                p2_choice = 'O'
                p = False
            else:
                p2_choice = 'X'
                p = False
        else:
            print('Please Select Write Choice X or O  To Continue')


def player_one():
    pos = input('Player Enter The Position Between 1-9 For Selection \n')
    try:
        pos = int(pos)
        if 0 < pos < 10:
            if my_list[pos] in ['X', 'O']:
                print('Entered Position Is Already Filled Try Out With Another Position')
                player_one()
            else:
                my_list[pos] = p1_choice
                p1_list.append(pos)
                rand_list.remove(pos)
        else:
            print('Please Enter a Number Between 1-9')
            player_one()
    except ValueError:
        print('Enter Only Integer Values')
        player_one()


def player_two():
    if 5 in rand_list:
        my_list[5] = p2_choice
        rand_list.remove(5)
        p2_list.append(5)
    else:
        z = win_con_ai()
        if z in rand_list:
            my_list[z] = p2_choice
            rand_list.remove(z)
            p2_list.append(z)
        else:
            pos = random.choice(rand_list)
            my_list[pos] = p2_choice
            rand_list.remove(pos)
            p2_list.append(pos)


def play_pos():
    global count
    if count == 0:
        player_two()
        print('')
        show()
        win_con(p2_list, 'Computer')

        if count == 0:
            if len(p1_list) + len(p2_list) < 9:
                player_one()
                print('')
                show()
                win_con(p1_list, 'Player')


def win_con(p_list, p_name):
    global p1
    global count
    print(p_list)

    if len(p_list) == 3:
        if tuple(p_list[:3]) in win_tup:
            print(f'{p_name} Is Winner')
            count = 1
            p1 = False

    if len(p_list) >= 4:
        for i in p_list:
            if tuple(p_list[:3]) in win_tup:
                print(f'{p_name} Is Winner')
                count = 1
                p1 = False
                break
            p_list.remove(i)
            p_list.sort()
            if tuple(p_list[:3]) in win_tup:
                print(f'{p_name} Is Winner')
                count = 1
                p1 = False
                break
            else:
                p_list.append(i)
                p_list.sort()

    if len(p_list) == 5:
        for i in range(4):
            if tuple(p_list[::2]) in win_tup:
                print(f'{p_name} Is Winner')
                count = 1
                p1 = False
                break
            t = p_list[i]
            t1 = p_list[i + 1]
            p_list.remove(t)
            p_list.remove(t1)
            if tuple(p_list[:3]) in win_tup:
                print(f'{p_name} Is Winner')
                count = 1
                p1 = False
                break
            else:
                p_list.append(t)
                p_list.append(t1)
                p_list.sort()

    if len(p1_list) + len(p2_list) == 9 and count == 0:
        print('Match Is Draw\n')
        p1 = False


def win_con_ai():
    global p1
    global count
    for k in rand_list:
        p2_list.append(k)
        if len(p2_list) == 3:
            if tuple(p2_list[:3]) in win_tup:
                p2_list.remove(k)
                return k

        if len(p2_list) >= 4:
            for i in p2_list:
                if tuple(p2_list[:3]) in win_tup:
                    return k
                p2_list.remove(i)
                p2_list.sort()
                if tuple(p2_list[:3]) in win_tup:
                    p2_list.remove(k)
                    return k
                else:
                    p2_list.append(i)
                    p2_list.sort()
        if len(p2_list) == 5:
            for i in range(4):
                if tuple(p2_list[::2]) in win_tup:
                    p2_list.remove(k)
                    return k
                t = p2_list[i]
                t1 = p2_list[i + 1]
                p2_list.remove(t)
                p2_list.remove(t1)
                if tuple(p2_list[:3]) in win_tup:
                    p2_list.remove(k)
                    return k
                else:
                    p2_list.append(t)
                    p2_list.append(t1)
                    p2_list.sort()
        p2_list.remove(k)
        p1_list.append(k)
        if len(p1_list) == 3:
            if tuple(p1_list[:3]) in win_tup:
                p1_list.remove(k)
                return k

        if len(p1_list) >= 4:
            for i in p1_list:
                if tuple(p1_list[:3]) in win_tup:
                    p1_list.remove(k)
                    return k
                p1_list.remove(i)
                p1_list.sort()
                if tuple(p1_list[:3]) in win_tup:
                    p1_list.remove(k)
                    return k
                else:
                    p1_list.append(i)
                    p1_list.sort()

        if len(p1_list) == 5:
            for i in range(4):
                if tuple(p1_list[::2]) in win_tup:
                    p1_list.remove(k)
                    return k
                t = p1_list[i]
                t1 = p1_list[i + 1]
                p1_list.remove(t)
                p1_list.remove(t1)
                if tuple(p1_list[:3]) in win_tup:
                    p1_list.remove(k)
                    return k
                else:
                    p1_list.append(t)
                    p1_list.append(t1)
                    p1_list.sort()
        p1_list.remove(k)
    else:
        return 0


while p1:
    print('')
    show()
    play_pos()
    if p1 is False:
        choice = input('Do You Want To Play Again Then Press Y or y Else press any Key')
        if choice in ['Y', 'y']:
            my_list = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9]
            p2_list.clear()
            p1_list.clear()
            p1, p, count = True, True, 0
