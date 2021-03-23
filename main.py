while True:
    distance = float(input('Distance : '))
    distance_choice = int(input('Which Unit did you use ? '
                                '\n1)Metre(m)\n2)Kilometre(Km) '
                                '\nType number of your choice :'))
    while distance_choice == 1 or distance_choice == 2:
        if distance_choice == 1:
            pass
        if distance_choice == 2:
            distance = distance * (10 ** 3)
        break
    else:
        print('please enter 1 or 2')
        distance_choice = int(input('Which Unit did you use ? '
                                    '\n1)Metre(m)\n2)Kilometre(Km) '
                                    '\nType number of your choice :'))

    time = float(input('time : '))
    if time != 0:
        time_choice = int(input('Which Unit did you use ? '
                                '\n1)second\n2)Minute\n3)Hour'
                                '\nType number of your choice :'))
        while time_choice == 1 or time_choice == 2 or time_choice == 3:
            if time_choice == 1:
                pass
            if time_choice == 2:
                time = time * 60
            if time_choice == 3:
                time = time * 3600
            break
        else:
            print('please enter 1,2 or 3')
            time_choice = int(input('Which Unit did you use ? '
                                    '\n1)second\n2)Minute\n3)Hour'
                                    '\nType number of your choice :'))
        print(f'The Speed is : {distance / time} m/s')
        answer = str(input('do you want speed in km/h?\n Answer: '))
        if answer == 'yes' or answer == 'km/h':
            print(f'Speed in km/h is : {(distance / time)*3.6} Km/h')
            print('\t\t\t\tThank you for using us!')
        else:
            print('\t\t\t\tThank you for using us!')
        break
    else:
        print("it's impossible to divide on 0! please enter a valid number")
