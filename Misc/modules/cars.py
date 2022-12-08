def load_car_list(file_name):
    car_list = []
    with open(file_name, 'r') as file:
        for line in file:
            car_list.append(tuple(line.strip().split(',')))
    return car_list

def load_car_dict(file_name):
    car_dict = {}
    with open(file_name, 'r') as file:
        for line in file:
            car = tuple(line.strip().split(','))
            car_dict[car[4]] = car
    return car_dict

def cars_with_make(car_list, make):
    return [car for car in car_list if car[0] == make]

def cars_with_color(car_list, color):
    return [car for car in car_list if car[2] == color]

def sort_by_year(car_list):
    for i in range(len(car_list)):
        for j in range(i+1, len(car_list)):
            if int(car_list[i][3]) > int(car_list[j][3]):
                car_list[i], car_list[j] = car_list[j], car_list[i]
    return car_list

def remove_car(car_dict, id):
    if id not in car_dict:
        raise KeyError('Car with id {} does not exist'.format(id))
    else:
        del car_dict[id]

def print_make_count(car_list):
    make_dict = {}
    for car in car_list:
        make = car[0]
        if make not in make_dict:
            make_dict[make] = 1
        else:
            make_dict[make] += 1
    for make, count in make_dict.items():
        print('{} {}'.format(make, count))

def write_to_file(car_dict, file_name):
    with open(file_name, 'w') as file:
        for car in car_dict.values():
            file.write(','.join(car) +'\n')

